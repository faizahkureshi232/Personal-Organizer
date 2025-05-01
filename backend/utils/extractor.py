from langchain_core.tools import tool
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3.2")

@tool
def extract_tasks_tool(text: str) -> str:
    """Extracts actionable tasks from a given input text."""
    prompt = f"Extract all actionable to-do tasks from the following message:\n{text}"
    return llm.invoke(prompt)

