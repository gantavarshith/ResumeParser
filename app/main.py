from fastapi import FastAPI, UploadFile, File
import shutil
import os

from .parser import extract_pdf_text, extract_docx_text
from .llm import extract_resume_data
from .schemas import ResumeSchema
import uuid
import json

app = FastAPI()

UPLOAD_DIR = "uploads"
RESULTS_DIR = "results"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if file.filename.endswith(".pdf"):
        text = extract_pdf_text(file_path)

    elif file.filename.endswith(".docx"):
        text = extract_docx_text(file_path)

    else:
        return {
            "error": "Unsupported file format"
        }

    try:
        extracted_data = extract_resume_data(text)
        
        result_id = str(uuid.uuid4())
        extracted_data["id"] = result_id
        
        result_path = os.path.join(RESULTS_DIR, f"{result_id}.json")
        with open(result_path, "w") as f:
            json.dump(extracted_data, f, indent=4)

        return extracted_data
    except Exception as e:
        return {
            "error": "Failed to extract resume data",
            "details": str(e)
        }

@app.get("/result/{query}")
async def get_result(query: str):
    result_path = os.path.join(RESULTS_DIR, f"{query}.json")
    if os.path.exists(result_path):
        with open(result_path, "r") as f:
            return json.load(f)

    query_lower = query.lower()
    for filename in os.listdir(RESULTS_DIR):
        if filename.endswith(".json"):
            path = os.path.join(RESULTS_DIR, filename)
            with open(path, "r") as f:
                data = json.load(f)
                if (data.get("name") and query_lower in data.get("name").lower()) or \
                   (data.get("email") and query_lower == data.get("email").lower()) or \
                   (data.get("phone") and query_lower in data.get("phone").lower()):
                    return data

    return {"error": f"No result found matching '{query}'"}

# @app.get("/results")
# async def list_results():
#     results = []
#     for filename in os.listdir(RESULTS_DIR):
#         if filename.endswith(".json") and not results:
#             result_path = os.path.join(RESULTS_DIR, filename)
#             with open(result_path, "r") as f:
#                 data = json.load(f)
#                 results.append({
#                     "id": data.get("id"),
#                     "name": data.get("name"),
#                     "filename": filename
#                 })
#     return results
