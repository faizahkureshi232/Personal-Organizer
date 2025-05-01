from backend.agents.langchain_agent import run_agent

def answer_query(question: str) -> str:
    prompt = (
        "You are the Smart Personal Organizer & Life Assistant. "
        "You can summarize emails, calendar events, drive files, and parse docs. "
        f"Answer: {question}"
    )
    return run_agent(prompt)