from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOllama
from backend.agents.tools import summarize_tool, extract_tasks_tool, add_to_calendar_tool, lookup_tool
from langchain.agents import AgentExecutor

llm = ChatOllama(model="llama3.2")
agent = initialize_agent(
    tools=[
        summarize_tool,
        extract_tasks_tool,
        add_to_calendar_tool,
        lookup_tool
    ],  # your list of tools
    llm=llm, 
    agent_type="ZERO_SHOT_REACT_DESCRIPTION",  # or any agent type you're using
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=10,  # Increase the number of iterations if needed
    max_time=600 
)


def run_agent(prompt):
    return agent.run(prompt)