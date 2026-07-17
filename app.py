import streamlit as st
import pandas as pd
import plotly.express as px
from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx
from chains.evaluate import extract_resume_data, extract_jd_data, analyze_match
from utils.score import calculate_weighted_score
from dotenv import load_dotenv
import os

load_dotenv()


st.set_page_config(page_title="AI Resume Evaluator", page_icon="🎯", layout="wide")

st.title("🎯 AI Resume Evaluator & Job Match Analyzer")
st.write("Analyze resume structural alignment against target Job Descriptions instantly using LangChain and Llama 3.3.")



col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF or DOCX format", type=["pdf", "docx"])
    
with col2:
    st.subheader("2. Target Job Description")
    jd_text = st.text_area("Paste the job description details here...", height=200)

if st.button("Evaluate Candidate Suitability", type="primary"):
    if not uploaded_file or not jd_text.strip():
        st.error("Please provide both a valid resume file and job description text.")
    else:
        with st.spinner("Processing document structures and running deep matching..."):
            # Step 1: Document Parsing
            file_ext = uploaded_file.name.split(".")[-1].lower()
            if file_ext == "pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = extract_text_from_docx(uploaded_file)
            
            # Step 2: Extract structured objects via LLM
            extracted_resume = extract_resume_data(resume_text)
            extracted_jd = extract_jd_data(jd_text)
            
            # Step 3: Run Match Engine Analysis
            analysis_result = analyze_match(extracted_resume, extracted_jd)
            
            # Step 4: Deterministic Scoring Calculation
            final_score = calculate_weighted_score(analysis_result)
            
            # --- RENDER RESULTS ---
            st.success("Analysis Complete!")
            st.divider()
            
            # Score Dashboard Layout
            metric_col1, metric_col2, metric_col3 = st.columns(3)
            with metric_col1:
                st.metric(label="Weighted ATS Match Score", value=f"{final_score}%")
            with metric_col2:
                st.metric(label="Match Verdict", value=str(analysis_result.verdict))
            with metric_col3:
                stars = int(final_score // 20)
                st.metric(label="Rating", value="⭐" * max(stars, 1))
                
            st.divider()
            
            # Visual Representation (Radar / Bar Chart Chart for Category Scores)
            st.subheader("📊 Fit Dimension Analysis")
            score_data = {
                "Evaluation Dimension": ["Skills", "Projects", "Experience", "Education", "Certifications"],
                "Score Value": [
                    analysis_result.skill_score,
                    analysis_result.project_score,
                    analysis_result.experience_score,
                    analysis_result.education_score,
                    analysis_result.certification_score
                ]
            }
            df_scores = pd.DataFrame(score_data)
            fig = px.line_polar(df_scores, r='Score Value', theta='Evaluation Dimension', line_close=True, range_r=[0,100])
            fig.update_traces(fill='tonext')
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed breakdowns
            col_left, col_right = st.columns(2)
            
            with col_left:
                st.markdown("### ✅ Matched Skills")
                for sk in analysis_result.matched_skills:
                    st.markdown(f"- `{sk}`")
                    
                st.markdown("### 📈 Core Strengths")
                for strength in analysis_result.strengths:
                    st.markdown(f"✓ {strength}")
            
            with col_right:
                st.markdown("### ❌ Missing Mission-Critical Skills")
                for sk in analysis_result.missing_skills:
                    st.markdown(f"- :red[`{sk}`]")
                    
                st.markdown("### 🛠️ Optimization Suggestions")
                for sug in analysis_result.suggestions:
                    st.markdown(f"💡 {sug}")
            
            st.divider()
            st.markdown("### 📝 Evaluator Reasoning Summary")
            st.info(analysis_result.reasoning)