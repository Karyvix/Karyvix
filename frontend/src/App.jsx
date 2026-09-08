import { useRef, useState } from "react";
import {
  FileText,
  Upload,
  Sparkles,
  ArrowRight,
  X,
  LoaderCircle,
} from "lucide-react";

import "./App.css";


function App() {

  const fileInputRef = useRef(null);

  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const handleFileChange = (event) => {

    const selectedFile = event.target.files[0];

    if (!selectedFile) {
      return;
    }

    if (selectedFile.type !== "application/pdf") {
      setError("Please upload a PDF resume.");
      return;
    }

    setError("");
    setFile(selectedFile);
  };


  const handleBrowse = () => {
    fileInputRef.current.click();
  };


  const removeFile = () => {
    setFile(null);
    fileInputRef.current.value = "";
  };


  const handleAnalyze = async () => {

    if (!file) {
      setError("Please upload your resume first.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter the job description.");
      return;
    }

    setError("");
    setLoading(true);


    const formData = new FormData();

    formData.append("file", file);
    formData.append("job_description", jobDescription);


    try {

      const response = await fetch(
        "http://127.0.0.1:8000/analysis/",
        {
          method: "POST",
          body: formData,
        }
      );


      const data = await response.json();


      if (!response.ok) {
        throw new Error(
          data.detail || "Something went wrong."
        );
      }


      console.log("Analysis Result:", data);

      alert("Analysis completed! Check the browser console.");

    } catch (error) {

      console.error(error);

      setError(
        error.message ||
        "Unable to connect to Karyvix."
      );

    } finally {

      setLoading(false);

    }
  };


  return (
    <div className="app">

      <header className="navbar">

        <div className="brand">

          <div className="brand-icon">
            <Sparkles size={18} />
          </div>

          <span>Karyvix</span>

        </div>


        <div className="navbar-badge">
          AI Career Intelligence
        </div>

      </header>


      <main className="hero">

        <section className="hero-content">

          <div className="eyebrow">
            <Sparkles size={15} />
            AI-POWERED CAREER ANALYSIS
          </div>


          <h1>
            Know exactly how
            <br />
            <span>job-ready</span> you are.
          </h1>


          <p className="hero-description">
            Upload your resume and paste a job description.
            Karyvix analyzes your fit, identifies skill gaps,
            and gives you actionable recommendations.
          </p>


          <div className="analysis-card">

            {/* Resume */}

            <div className="upload-section">

              <div className="section-label">
                <FileText size={17} />
                Your Resume
              </div>


              <input
                ref={fileInputRef}
                type="file"
                accept=".pdf,application/pdf"
                onChange={handleFileChange}
                hidden
              />


              {!file ? (

                <div
                  className="upload-box"
                  onClick={handleBrowse}
                >

                  <div className="upload-icon">
                    <Upload size={22} />
                  </div>


                  <div>

                    <h3>
                      Upload your resume
                    </h3>

                    <p>
                      PDF files only
                    </p>

                  </div>


                  <button
                    className="browse-button"
                    type="button"
                    onClick={(event) => {
                      event.stopPropagation();
                      handleBrowse();
                    }}
                  >
                    Browse
                  </button>

                </div>

              ) : (

                <div className="upload-box file-selected">

                  <div className="upload-icon">
                    <FileText size={22} />
                  </div>


                  <div className="selected-file">

                    <h3>
                      {file.name}
                    </h3>

                    <p>
                      {(file.size / 1024 / 1024).toFixed(2)} MB
                    </p>

                  </div>


                  <button
                    className="remove-button"
                    type="button"
                    onClick={removeFile}
                    title="Remove resume"
                  >
                    <X size={18} />
                  </button>

                </div>

              )}

            </div>


            <div className="divider">
              <span>AND</span>
            </div>


            {/* Job Description */}

            <div className="job-section">

              <div className="section-label">
                <FileText size={17} />
                Job Description
              </div>


              <textarea
                value={jobDescription}
                onChange={(event) =>
                  setJobDescription(event.target.value)
                }
                placeholder="Paste the job description here..."
              />

            </div>


            {/* Error */}

            {error && (
              <div className="error-message">
                {error}
              </div>
            )}


            {/* Analyze */}

            <button
              className="analyze-button"
              type="button"
              onClick={handleAnalyze}
              disabled={loading}
            >

              {loading ? (
                <>
                  <LoaderCircle
                    size={18}
                    className="spinner"
                  />

                  Analyzing Resume...
                </>
              ) : (
                <>
                  Analyze My Resume
                  <ArrowRight size={18} />
                </>
              )}

            </button>

          </div>

        </section>

      </main>

    </div>
  );
}


export default App;