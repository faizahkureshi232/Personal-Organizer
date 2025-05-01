from langchain_core.tools import tool
from langchain_community.chat_models import ChatOllama
from langchain.tools import Tool
llm = ChatOllama(model="llama3.2")

@tool
def summarize_document(text: str) -> str:
    """
    Summarizes the provided text input.

    Args:
    - text (str): The input text to summarize.

    Returns:
    - str: The summarized version of the input text.
    """
    # Implement your summarization logic here
    return f"Summary of: {text}"

# Explicitly define the tool description if not using the decorator directly in Tool()
summarize_tool = Tool(
    name="SummarizeDocument",
    func=summarize_document,  # function to summarize text
    description="Summarizes documents or unstructured text. Input should be a plain string."
)


