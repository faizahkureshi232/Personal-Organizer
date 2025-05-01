from langchain_core.tools import tool
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3.2")

@tool
def add_to_calendar_tool(event_info: str) -> str:
    """Parses event details from the input and formats it for calendar addition."""
    prompt = f"Convert the following event information into a calendar-friendly format:\n{event_info}"
    return llm.invoke(prompt)
