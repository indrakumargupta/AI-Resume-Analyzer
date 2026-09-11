import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeResume = async () => {
    if (!file) {
      setError("Please select a PDF resume.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://localhost:8000/analyze",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong");
      }

      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Resume Analyzer</h1>

      <p className="subtitle">
        Upload your resume and get an AI-powered ATS analysis.
      </p>

      <div className="upload-box">
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        {file && (
          <p className="filename">
            Selected: {file.name}
          </p>
        )}

        <button onClick={analyzeResume} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </div>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result">
          <div className="score">
            <span>{result.score}</span>
            <small>/ 100</small>
          </div>

          <h2>Summary</h2>
          <p>{result.summary}</p>

          <h2>Skills</h2>
          <div className="tags">
            {result.skills.map((skill, index) => (
              <span key={index}>{skill}</span>
            ))}
          </div>

         < h2>Role</h2>
          <p>{result.Role}</p>

          <h2>Strengths</h2>
          <ul>
            {result.strengths.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h2>Missing Skills</h2>
          <ul>
            {result.missing_skills.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h2>Suggestions</h2>
          <ul>
            {result.suggestions.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
