from pydantic import BaseModel, Field
from typing import List, Optional

class ResumeSchema(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address of the candidate")
    phone: str = Field(description="Phone number or contact details")
    skills: List[str] = Field(default=[], description="List of technical and soft skills extracted")
    education: List[str] = Field(default=[], description="List of degrees, universities, and graduation years")
    experience: List[str] = Field(default=[], description="List of past jobs, roles, companies, and durations")
    projects: List[str] = Field(default=[], description="List of projects mentioned with brief descriptions")
    certifications: List[str] = Field(default=[], description="List of certifications or licenses")