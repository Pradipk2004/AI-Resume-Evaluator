from pydantic import BaseModel, Field
from typing import List

class MatchResultSchema(BaseModel):
    skill_score: int = Field(description="Score from 0 to 100 assessing how well candidate skills match the JD")
    project_score: int = Field(description="Score from 0 to 100 assessing the relevance of candidate projects to the JD")
    experience_score: int = Field(description="Score from 0 to 100 assessing if experience depth/relevance matches requirements")
    education_score: int = Field(description="Score from 0 to 100 evaluating academic alignment")
    certification_score: int = Field(description="Score from 0 to 100 evaluating relevant certifications")
    verdict: str = Field(description="Short phrase: Excellent Match, Good Match, Partial Match, or Low Alignment")
    matched_skills: List[str] = Field(description="Skills present in both the resume and the job description")
    missing_skills: List[str] = Field(description="Important skills from the job description missing from the resume")
    strengths: List[str] = Field(description="Bullet points of the candidate's core alignments")
    weaknesses: List[str] = Field(description="Areas where the candidate falls short of the requirements")
    suggestions: List[str] = Field(description="Actionable steps the candidate can take to improve their resume or profile for this job")
    reasoning: str = Field(description="A concise summary explaining the scores and evaluation")