from backend.service.google_auth_env import get_service

def fetch_drive_files():
    service = get_service('drive', 'v3')
    results = service.files().list(pageSize=5, fields="files(name)").execute()
    items = results.get('files', [])
    return [f['name'] for f in items]

# backend/services/chat_services.py
from backend.agents.langchain_agent import run_agent

def answer_query(question: str) -> str:
    prompt = (
        "You are the Smart Personal Organizer & Life Assistant. "
        "You can summarize emails, calendar events, drive files, and parse docs. "
        f"Answer: {question}"
    )
    return run_agent(prompt)