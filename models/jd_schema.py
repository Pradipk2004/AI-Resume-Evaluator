from pydantic import BaseModel, Field
from typing import List

class JobDescriptionSchema(BaseModel):
    title: str = Field(description="The job title")
    required_skills: List[str] = Field(default=[], description="Core skills explicitly required for the role")
    preferred_skills: List[str] = Field(default=[], description="Optional or preferred skills mentioned")
    education: List[str] = Field(default=[], description="Minimum or preferred educational requirements")
    experience: str = Field(description="Years or depth of experience required")