from langchain.tools import Tool
from backend.utils import summarizer, extractor
from backend.service  import calendar_service

summarize_tool = Tool(name="SummarizeDocument", func=summarizer.summarize_tool, description="Summarizes document text")
extract_tasks_tool = Tool(name="ExtractTasks", func=extractor.extract_tasks_tool, description="Extracts tasks")
add_to_calendar_tool = Tool(name="AddToCalendar", func=calendar_service.create_event, description="Schedules event")
lookup_tool = Tool(name="MemoryLookup", func=lambda x: "Search feature not implemented", description="Looks up past summaries")