🤖 AI Resume Analyzer

An AI-powered resume analysis application that helps job seekers analyze and improve their resumes using Google Gemini AI.

The application provides AI-generated insights about resume quality, strengths, weaknesses, skills, keywords, and areas for improvement.

🌟 Features
📄 Resume upload
🤖 AI-powered resume analysis
🧠 Google Gemini integration
📊 Resume scoring
💪 Strength identification
⚠️ Weakness identification
🔑 Keyword and skill analysis
💡 Actionable improvement suggestions
🎨 Modern and responsive UI
⚡ FastAPI backend
⚛️ React frontend
🖥️ Tech Stack
Frontend
React.js
JavaScript
HTML5
CSS3
Vite
Backend
Python
FastAPI
Uvicorn
AI
Google Gemini API
Development Tools
Git
GitHub
npm
Python Virtual Environment
📁 Project Structure
AI-Resume-Analyzer/
│
├── Backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── Frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── .gitignore
├── README.md
└── ...

🚀 Installation & Setup
1. Prerequisites

Before running the project, make sure you have installed:

Git
Python 3.10+
Node.js 18+
npm
A Google Gemini API key

Check the installed versions:

git --version
python --version
node --version
npm --version

📥 2. Clone the Repository

Open your terminal or command prompt and run:

git clone https://github.com/indrakumargupta/AI-Resume-Analyzer.git


Move into the project directory:

cd AI-Resume-Analyzer


You can verify the files using:

dir


On macOS/Linux:

ls

🐍 3. Backend Setup

Open a terminal inside the project directory.

Go to the backend:

cd Backend

Create a virtual environment
Windows
python -m venv venv


Activate it:

venv\Scripts\activate

macOS / Linux
python3 -m venv venv


Activate it:

source venv/bin/activate


After activation, you should see something similar to:

(venv)


in your terminal.

📦 4. Install Backend Dependencies

Make sure you are inside the Backend directory:

cd Backend


Install the required Python packages:

pip install -r requirements.txt


If pip does not work, try:

python -m pip install -r requirements.txt

🔐 5. Configure Gemini API Key

The application uses Google Gemini for AI-powered resume analysis.

Create a .env file inside the Backend folder:

Backend/
└── .env


Add:

GEMINI_API_KEY=your_gemini_api_key


Replace:

your_gemini_api_key


with your actual Gemini API key.

⚠️ Never upload your .env file to GitHub.

▶️ 6. Start the Backend

From the Backend directory:

uvicorn main:app --reload


Or:

python -m uvicorn main:app --reload


If everything is configured correctly, you should see something similar to:

Uvicorn running on http://127.0.0.1:8000


Backend API:

http://127.0.0.1:8000


FastAPI Swagger documentation:

http://127.0.0.1:8000/docs


You can open the Swagger documentation in your browser to test the API.

⚛️ 7. Frontend Setup

Open a new terminal.

Go back to the project root:

cd AI-Resume-Analyzer


Then:

cd Frontend


Install frontend dependencies:

npm install

▶️ 8. Start the Frontend

Run:

npm run dev


Vite will display a local development URL, usually similar to:

http://localhost:5173


Open that URL in your browser.

🔄 Complete Setup

You should have two terminals running.

Terminal 1 — Backend
cd AI-Resume-Analyzer
cd Backend

venv\Scripts\activate

uvicorn main:app --reload

Terminal 2 — Frontend
cd AI-Resume-Analyzer
cd Frontend

npm install
npm run dev


Then open the frontend URL shown by Vite.

🔁 How the Application Works
                 USER
                  │
                  ▼
        ┌──────────────────┐
        │  React Frontend  │
        └────────┬─────────┘
                 │
                 │ HTTP Request
                 ▼
        ┌──────────────────┐
        │  FastAPI Backend │
        └────────┬─────────┘
                 │
                 │ Resume Data
                 ▼
        ┌──────────────────┐
        │   Google Gemini  │
        │       AI         │
        └────────┬─────────┘
                 │
                 │ AI Analysis
                 ▼
        ┌──────────────────┐
        │  FastAPI Backend │
        └────────┬─────────┘
                 │
                 │ JSON Response
                 ▼
        ┌──────────────────┐
        │  React Dashboard │
        └──────────────────┘

📊 Resume Analysis

The application can analyze different aspects of a resume, including:

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
Professional summary
Work experience
Projects
Education
Certifications
Improvement Suggestions

The AI provides suggestions such as:

✓ Add measurable achievements

✓ Improve the professional summary

✓ Highlight relevant technical skills

✓ Add stronger action verbs

✓ Remove unnecessary information

🔑 Environment Variables

Create:

Backend/.env


Example:

GEMINI_API_KEY=your_gemini_api_key


For production, environment variables should be configured through your hosting provider instead of committing secrets to the repository.

🚫 .gitignore

Make sure sensitive and unnecessary files are not committed.

Example:

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

🧪 API

The backend is built using FastAPI.

Once the backend is running, open:

http://127.0.0.1:8000/docs


This opens the interactive Swagger UI where available API endpoints can be tested directly.

🛠️ Development

If you make changes to the backend, uvicorn --reload automatically reloads the server.

For frontend development:

npm run dev


For a production frontend build:

npm run build


The generated production files will be placed in the Vite build directory.

🐛 Troubleshooting
git command not found

Install Git and restart your terminal.

Check:

git --version

python command not found

Install Python and make sure Python is added to your system PATH.

Check:

python --version


On some systems:

python3 --version

npm command not found

Install Node.js.

Check:

node --version
npm --version

Gemini API error

Check that:

GEMINI_API_KEY


is correctly configured in:

Backend/.env


Also make sure the API key is valid and has access to the required Gemini API.

Backend is not connecting to frontend

Make sure the backend is running:

http://127.0.0.1:8000


and the frontend is running on the Vite development URL.

If required, check the frontend API/base URL configuration.

ModuleNotFoundError

Make sure the virtual environment is activated:

Windows
venv\Scripts\activate


Then reinstall dependencies:

pip install -r requirements.txt

🔒 Security & Privacy

Resumes can contain personal and sensitive information.

For production deployment:

Never expose your Gemini API key in frontend code.
Keep API keys in environment variables.
Never commit .env files.
Validate uploaded files.
Restrict allowed file types and file sizes.
Avoid permanently storing resumes unless necessary.
Delete uploaded files when they are no longer required.
Use HTTPS in production.
Add authentication and authorization if storing user data.
🚀 Future Improvements

Some planned improvements include:

🎯 Resume vs Job Description matching
📊 Advanced ATS scoring
🔍 Semantic keyword matching
🧠 Skill-gap analysis
✍️ AI-powered resume rewriting
📝 AI-generated professional summary
📈 Section-wise scoring
📥 Downloadable PDF analysis reports
👤 User authentication
🗂️ Resume history
☁️ Cloud deployment
🔒 Enhanced privacy controls
📱 Improved mobile experience
🤝 Contributing

Contributions are welcome!

1. Fork the repository

Click the Fork button on GitHub.

2. Clone your fork
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git

3. Enter the project
cd AI-Resume-Analyzer

4. Create a new branch
git checkout -b feature/your-feature

5. Make your changes

Implement your feature or bug fix.

6. Commit your changes
git add .
git commit -m "Add your feature"

7. Push your branch
git push origin feature/your-feature

8. Create a Pull Request

Open the repository on GitHub and create a Pull Request.

⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.

It helps support the project and encourages further development.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Indra Kumar Gupta

GitHub:

https://github.com/indrakumargupta

📌 Disclaimer
AI-generated resume analysis is intended to provide guidance and suggestions.
Resume scores and recommendations should not be considered a guarantee of ATS performance, interview selection, or employment.
AI-generated resume analysis is intended to provide guidance and suggestions.

Resume scores and recommendations should not be considered a guarantee of ATS performance, interview selection, or employment.
