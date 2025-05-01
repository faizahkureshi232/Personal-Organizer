from fastapi import APIRouter, File, UploadFile
from backend.utils.parser import parse
from backend.utils.summarizer import summarize
from backend.utils.extractor import extract_tasks

import os

@router.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...)):
    content = await parse(file)
    summary = summarize(content)
    tasks = extract_tasks(summary)
    return {"summary": summary, "tasks": tasks}
