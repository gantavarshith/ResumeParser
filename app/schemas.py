from pydantic import BaseModel
from typing import List, Optional

class ProjectSchema(BaseModel):
    name: str
    description: Optional[str] = None
    year: Optional[str] = None

class ExperienceSchema(BaseModel):
    title: str
    company: str
    duration: Optional[str] = None
    description: Optional[str] = None

class EducationSchema(BaseModel):
    degree: str
    institution: Optional[str] = None
    year: Optional[str] = None
    score: Optional[str] = None

class ResumeSchema(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    skills: List[str] = []
    projects: List[ProjectSchema] = []
    experience: List[ExperienceSchema] = []
    education: List[EducationSchema] = []
