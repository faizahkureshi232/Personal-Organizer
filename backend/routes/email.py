from fastapi import APIRouter
from backend.service.gmail_service import fetch_emails_summary

from backend.utils import summarizer, extractor

router = APIRouter()

@router.get("/summarize-emails")
def summarize_emails():
    summaries = fetch_emails_summary()
    return {"summaries": summaries}
