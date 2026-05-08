PROMPT_TEMPLATE = """
You are a highly accurate resume parsing assistant. Your task is to extract structured information from the provided resume text.

### Extraction Rules:
1. **name**: Full name of the candidate.
2. **email**: Contact email address.
3. **phone**: Contact phone number.
4. **skills**: A list of technical and soft skills (strings).
5. **projects**: A list of objects. Each object must have:
   - "name": Project name
   - "description": Brief description
   - "year": Duration or year (e.g. "2022")
6. **experience**: A list of objects. Each object must have:
   - "title": Job title
   - "company": Company name
   - "duration": Time period (e.g. "2020-2023")
   - "description": Key responsibilities
7. **education**: A list of objects. Each object must have:
   - "degree": Degree name
   - "institution": School or University name
   - "year": Graduation year
   - "score": GPA, CGPA or Percentage

### Output Format:
Return ONLY a strictly valid JSON object. Ensure all keys ("name", "email", "phone", "skills", "projects", "experience", "education") are present. Use empty arrays [] if no data is found for a section.

Resume Text:
{text}
"""
