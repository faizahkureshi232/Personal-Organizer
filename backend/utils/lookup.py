from langchain_core.tools import tool
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3.2")

@tool
def lookup_tool(query: str) -> str:
    """Looks up general knowledge or recent information related to the query."""
    prompt = f"Answer the following query as accurately as possible:\n{query}"
    return llm.invoke(prompt)
