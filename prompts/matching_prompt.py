from langchain_core.prompts import ChatPromptTemplate

RESUME_EXTRACTION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert ATS (Applicant Tracking System) parser. Extract all requested information from the unstructured resume text into the requested structured schema."),
    ("human", "Resume Text:\n\n{text}")
])

JD_EXTRACTION_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert technical recruiter. Extract the key job details, required skills, and constraints from this job description text into the requested structured schema."),
    ("human", "Job Description Text:\n\n{text}")
])

MATCHING_PROMPT = ChatPromptTemplate.from_messages([
    ("system", (
        "You are an elite Technical Hiring Manager. Compare the provided structured Resume JSON against the Job Description JSON.\n"
        "Evaluate the following dimensions independently, giving a score from 0 (no match) to 100 (perfect fit) for each:\n"
        "1. skill_score\n"
        "2. project_score\n"
        "3. experience_score\n"
        "4. education_score\n"
        "5. certification_score\n\n"
        "Be highly rigorous, objective, and accurate. Do not hallucinate skills."
    )),
    ("human", "Candidate Resume Info:\n{resume_json}\n\nJob Requirements:\n{jd_json}")
])