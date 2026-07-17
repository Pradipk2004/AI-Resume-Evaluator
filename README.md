# 🎯 AI Resume Evaluator & Job Match Analyzer

An enterprise-grade generative AI tool built using **LangChain**, **Groq (Llama 3.3 70B)**, **Pydantic**, and **Streamlit**. This application parses resumes (PDF/DOCX), processes them alongside job descriptions, extracts structured intelligence via deterministic JSON schemas, and scores their fit using explicit, rule-based business logic.

---

## 🚀 Key Features

* **Multi-Format Parsing Engine:** Supports instant plain-text extraction from both `.pdf` and `.docx` document formats using dedicated `pdfplumber` and `python-docx` scripts.
* **Deterministic Schema Extraction:** Leverages LangChain's `.with_structured_output()` explicitly bound to strict Pydantic schemas, eliminating LLM hallucination and guaranteeing reliable data processing.
* **Hybrid Weighted Scoring Guardrail:** Instead of relying on unpredictable LLM scoring, the application applies strict programmatic weights to individual dimensions (Skills 50%, Projects 20%, Experience 15%, Education 10%, Certifications 5%) for explainable, stable ATS matching.
* **Dynamic Analytics Dashboard:** Visualizes fit dimension alignment using an interactive radar chart built with Plotly.
* **Granular Gap Analysis:** Identifies core alignments, actionable optimization adjustments, missing mission-critical skills, and full evaluator logic summaries.

---

## 🏗️ Project Architecture

The application acts as a linear, structured data parsing pipeline:

```text
                     User
                       │
            Upload Resume (PDF/DOCX)
                       │
                       ▼
             Resume Parser Module
        (pdfplumber / python-docx)
                       │
              Clean Resume Text
                       │
        Paste Job Description Text
                       │
                       ▼
            JD Information Extractor
           (Pydantic + LangChain)
                       │
                       ▼
        Resume Information Extractor
          (Pydantic + LangChain)
                       │
                       ▼
            Structured JSON Objects
                       │
                       ▼
             Matching Engine (LLM)
                       │
           Multi-Dimension Scoring
                       │
                       ▼
             Final Score Generator
          (Deterministic Weights Calculation)
                       │
                       ▼
              Streamlit Dashboard
```

---

## 📁 Repository Structure

```text
resume-evaluator/
│
├── app.py                  # Core Streamlit UI entrypoint
├── requirements.txt        # System dependency declaration
├── .env.example            # Environment variables placeholder
├── README.md               # Documentation guide
│
├── parser/                 # File structural parsing scripts
│   ├── pdf_parser.py
│   └── docx_parser.py
│
├── models/                 # Pydantic JSON structure schemas
│   ├── resume_schema.py
│   ├── jd_schema.py
│   └── result_schema.py
│
├── prompts/                # Chat templates configuration
│   └── matching_prompt.py
│
├── chains/                 # LangChain orchestration execution modules
│   └── evaluate.py
│
└── utils/                  # Non-LLM business logic configurations
    └── score.py
```
