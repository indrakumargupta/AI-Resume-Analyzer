# 🤖 AI Resume Analyzer

An AI-powered resume analysis application that helps job seekers analyze and improve their resumes using Google Gemini AI.

## ✨ Features

- 📄 Resume Upload
- 🤖 AI-powered Resume Analysis
- 🧠 Google Gemini Integration
- 📊 Resume Scoring
- 💪 Strength Identification
- ⚠️ Weakness Identification
- 🔑 Keyword & Skill Analysis
- 💡 Actionable Improvement Suggestions
- 🎨 Modern & Responsive UI
- ⚡ FastAPI Backend
- ⚛️ React Frontend

## 🛠️ Tech Stack

### Frontend

- React.js
- JavaScript
- HTML5
- CSS3

### Backend

- Python
- FastAPI

### AI

- Google Gemini API

### Tools

- Git
- GitHub

---

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── Backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── Frontend/
│   ├── src/
│   │      ├── assest/
│   │      ├── App.css
│   │      ├── App.jsx
│   │      ├── index.css
│   │      └── main.jsx
│   ├── public/
│   ├── index.html
│   ├── package.json 
│   ├── .gitignore
│   ├── package-lock.json
│   └── ...
│
├── .gitignore
└── README.md
```

🚀 Getting Started
Follow these steps to run the project locally.

1. Prerequisites
Make sure you have the following installed:

Git
Python 3.10+
Node.js 18+
npm
Google Gemini API Key
Check your installed versions:
git --version
python --version
node --version
npm --version


 2. Clone the Repository
Open your terminal and run:

git clone https://github.com/indrakumargupta/AI-Resume-Analyzer.git

Go inside the project:

cd AI-Resume-Analyzer

🐍 3. Backend Setup
Go to the Backend directory:

cd Backend

Create Virtual Environment
Windows
python -m venv venv

Activate it:

venv\Scripts\activate

macOS / Linux
python3 -m venv venv

Activate it:

source venv/bin/activate

📦 4. Install Backend Dependencies
Inside the Backend directory:

pip install -r requirements.txt

If pip doesn't work:

python -m pip install -r requirements.txt

🔐 5. Configure Gemini API
Create a .env file inside the Backend folder:

Backend/
└── .env

Add your Gemini API key:

GEMINI_API_KEY=your_gemini_api_key

⚠️ Never commit your .env file to GitHub.

▶️ 6. Run the Backend
Start the FastAPI server:

uvicorn main:app --reload

Or:

python -m uvicorn main:app --reload

Backend will run at:

http://127.0.0.1:8000

FastAPI Swagger documentation:

http://127.0.0.1:8000/docs

⚛️ 7. Frontend Setup
Open a new terminal.

Go back to the project:

cd AI-Resume-Analyzer

Go to the frontend:

cd Frontend

Install dependencies:

npm install

▶️ 8. Run the Frontend
Start the React/Vite development server:

npm run dev

Vite will show a URL similar to:

http://localhost:5173

Open that URL in your browser.

🔄 How It Works
User
  │
  ▼
React Frontend
  │
  │ HTTP Request
  ▼
FastAPI Backend
  │
  │ Resume Data
  ▼
Google Gemini AI
  │
  │ AI Analysis
  ▼
FastAPI Backend
  │
  │ JSON Response
  ▼
React Dashboard

📊 Resume Analysis
The application analyzes different aspects of a resume.

Resume Quality
Overall resume quality
Content quality
Professional presentation
Relevance of information
Skills
Technical skills
Soft skills
Relevant technologies
Skill gaps
Content
Professional Summary
Work Experience
Projects
Education
Certifications
AI Recommendations
The application can provide suggestions such as:

✓ Add measurable achievements

✓ Improve the professional summary

✓ Highlight relevant technical skills

✓ Use stronger action verbs

✓ Remove unnecessary information

🔐 Environment Variables
Create:

Backend/.env

Example:

GEMINI_API_KEY=your_gemini_api_key

Never push API keys or other secrets to GitHub.

🚫 .gitignore
Recommended .gitignore:

# Environment variables
.env
.env.*

# Python
__pycache__/
*.py[cod]
venv/
.venv/

# Node
node_modules/
dist/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

🧪 API Documentation
The backend uses FastAPI.

After starting the backend, open:

http://127.0.0.1:8000/docs

FastAPI provides an interactive Swagger UI where you can test the available API endpoints.

🐛 Troubleshooting
Python not found
Check:

python --version

If it doesn't work, install Python and add it to your PATH.

npm not found
Check:

node --version
npm --version

Install Node.js if required.

Gemini API Error
Check that your .env contains:

GEMINI_API_KEY=your_gemini_api_key

Also make sure your API key is valid.

ModuleNotFoundError
Activate your virtual environment:

venv\Scripts\activate

Then install dependencies again:

pip install -r requirements.txt

🚀 Future Improvements
🎯 Resume vs Job Description Matching
📊 Advanced ATS Scoring
🔍 Semantic Keyword Matching
🧠 Skill Gap Analysis
✍️ AI Resume Rewriting
📝 AI-generated Professional Summary
📈 Section-wise Resume Scoring
📥 Downloadable Analysis Report
👤 User Authentication
🗂️ Resume History
☁️ Cloud Deployment
🔒 Enhanced Privacy Controls
📱 Improved Mobile Experience
🤝 Contributing
Contributions are welcome!

1. Fork the Repository
Click the Fork button on GitHub.

2. Clone Your Fork
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git

3. Enter the Project
cd AI-Resume-Analyzer

4. Create a Branch
git checkout -b feature/your-feature

5. Make Changes
Implement your feature or fix.

6. Commit Changes
git add .
git commit -m "Add your feature"

7. Push Changes
git push origin feature/your-feature

8. Create a Pull Request
Open your fork on GitHub and create a Pull Request.

🔒 Security & Privacy
Resumes may contain sensitive personal information.

For production deployment:

Never expose API keys in frontend code.
Keep secrets in environment variables.
Never commit .env files.
Validate uploaded files.
Restrict file types and file sizes.
Avoid permanently storing resumes unless required.
Delete uploaded files when no longer needed.
Use HTTPS in production.
⭐ Support
If you like this project, please consider giving it a ⭐ on GitHub.

👨‍💻 Author
Indra Kumar Gupta

GitHub:
https://github.com/indrakumargupta

📄 License
This project is licensed under the MIT License.

⚠️ Disclaimer
AI-generated resume analysis is intended for guidance and informational purposes only.

Resume scores and recommendations do not guarantee ATS performance, interview selection, or employment.
