import os
import json 
from io import BytesIO


from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
from google import genai

load_dotenv() 

app = FastAPI(title="AI Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract_text(pdf_bytes: bytes) -> str:
    reader = PdfReader(BytesIO(pdf_bytes))

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    return text


@app.get("/")
def home():
    return {"message": "Resume Analyzer API is running"}


@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF resume"
        )

    pdf_bytes = await file.read()

    try:
        resume_text = extract_text(pdf_bytes)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Could not read PDF"
        )

    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="No readable text found in resume"
        )

    prompt = f"""
You are an expert ATS resume analyzer.

Also identify whether the candidate is better suited for Machine Learning or Web Development or roles and provide a brief reason based on their skills and experience.


Analyze the following resume and return ONLY valid JSON.

Resume:
{resume_text}

Return exactly this structure:

{{
  "score": 0,
  "summary": "",
  "skills": [],
  "Role":[],
  "strengths": [],
  "missing_skills": [],
  "suggestions": []
}}

Rules:
- score must be between 0 and 100
- skills should contain technical/professional skills
- strengths should contain important positive points
- missing_skills should contain useful skills that could improve the resume
- suggestions should be practical and concise
"""


    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        result = response.text.strip()

        # Remove markdown JSON fences if Gemini returns them
        if result.startswith("```"):
            result = result.replace("```json", "")
            result = result.replace("```", "")
            result = result.strip()

        analysis = json.loads(result)

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="AI returned invalid JSON"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )

    return analysis
