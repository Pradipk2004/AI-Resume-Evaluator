import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from models.resume_schema import ResumeSchema
from models.jd_schema import JobDescriptionSchema
from models.result_schema import MatchResultSchema
from prompts.matching_prompt import RESUME_EXTRACTION_PROMPT, JD_EXTRACTION_PROMPT, MATCHING_PROMPT

load_dotenv()

print("Loaded evaluate.py:", __file__)

def get_llm():
    print("Creating ChatGroq with llama-3.3-70b-versatile")
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        groq_api_key=os.getenv("GROQ_API_KEY"),
    )

def extract_resume_data(text: str) -> ResumeSchema:
    llm = get_llm()
    structured_llm = llm.with_structured_output(ResumeSchema)
    chain = RESUME_EXTRACTION_PROMPT | structured_llm
    return chain.invoke({"text": text})

def extract_jd_data(text: str) -> JobDescriptionSchema:
    llm = get_llm()
    structured_llm = llm.with_structured_output(JobDescriptionSchema)
    chain = JD_EXTRACTION_PROMPT | structured_llm
    return chain.invoke({"text": text})

def analyze_match(resume_obj: ResumeSchema, jd_obj: JobDescriptionSchema) -> MatchResultSchema:
    llm = get_llm()
    structured_llm = llm.with_structured_output(MatchResultSchema)
    chain = MATCHING_PROMPT | structured_llm
    
    return chain.invoke({
        "resume_json": resume_obj.model_dump_json(),
        "jd_json": jd_obj.model_dump_json()
    })