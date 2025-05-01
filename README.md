🧠 Smart Personal Organizer & Life Assistant
============================================

A full-stack AI-powered productivity assistant that leverages LangChain agents, Ollama llama3.2, Google APIs (Gmail, Calendar, Drive), OCR, and vector search to:

-   Summarize emails, PDFs, and DOCX files

-   Extract actionable tasks and events

-   Schedule reminders via Google Calendar

-   Answer follow-up questions about documents and agenda

-   Maintain memory and context across conversations

* * * * *

🏗️ Project Structure
---------------------

```gql
smart-assistant/
│
├── backend/
│   ├── main.py                    # FastAPI server entry point
│   ├── routes/
│   │   ├── document.py            # Document upload, parsing, and summarization
│   │   ├── email.py               # Gmail API integration and email summarization
│   │   ├── calendar.py            # Google Calendar event creation
│   │   └── chat.py                # Chat endpoint using LangChain agent
│   ├── agents/
│   │   ├── langchain_agent.py     # Tool-using agent with task-specific tools
│   │   ├── tools.py               # Custom LangChain tools (PDF parser, task extractor, etc.)
│   │   └── memory.py              # Memory management using ConversationBufferMemory
│   ├── service/
│   │   ├── gmail_service.py       # Gmail API wrapper (OAuth2, read emails)
│   │   ├── calendar_service.py    # Google Calendar API wrapper (create/update events)
│   │   └── drive_service.py       # Google Drive file access
│   └── utils/
│       ├── parser.py              # PDF, DOCX parsing; OCR using pytesseract
│       ├── summarizer.py          # Summarization with OpenAI GPT-4
│       └── extractor.py           # Extract to-dos from summaries (OpenAI function calls)
│
├── frontend/
│   ├── app.py                     # Streamlit app entry point
│   └── components/
│       ├── uploader.py            # File uploader UI
│       ├── email_viewer.py        # Display summarized emails
│       ├── calendar_view.py       # Calendar interface and reminders
│       └── chat_box.py            # Memory-based chat interface
│
├── vector_store/
│   ├── faiss_index.pkl           # FAISS vector store for storing document chunks
│
├── .env                           # API keys and OAuth2 credentials
├── requirements.txt               # Python dependencies
└── README.md                      # You are here`
```
* * * * *

🚀 Setup & Run Instructions
---------------------------

### 1\. 🔐 API Keys

Create a `.env` file with the following keys:

```env

# === GOOGLE API CONFIGURATION ===
GOOGLE_CLIENT_ID=xxx
GOOGLE_CLIENT_SECRET=xxx
GOOGLE_REFRESH_TOKEN=xxx
GMAIL_SCOPES=xxx
CALENDAR_SCOPES=xxx
DRIVE_SCOPES=xxx
GOOGLE_TOKEN_URI=xxx

# === LANGCHAIN CONFIG ===
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=xxx
LANGSMITH_API_KEY=xxx
LANGSMITH_PROJECT="SmartOrganizer"

# === FRONTEND / BACKEND CONFIG ===

# Backend server port
BACKEND_PORT=8000

# Frontend streamlit port (if separate)
FRONTEND_PORT=8501


# === DEBUG / LOGGING SETTINGS ===
DEBUG=true
LOG_LEVEL=INFO
```

> Note: Use OAuth2 for Google API access to Gmail, Calendar, and Drive. Set up scopes and consent screen in the Google Cloud Console.

* * * * *

### 2\. 📦 Install Dependencies

```env 
pip install -r requirements.txt
```

* * * * *

### 3\. 🖥️ Run FastAPI Backend

```env 
cd backend
uvicorn main:app --reload
```

APIs served at `http://localhost:8000`.

* * * * *

### 4\. 🖼️ Run the Project

```env
./start_project.sh    
```

* * * * *

🔄 Workflow Breakdown
---------------------

### Step 1: 📤 Document Upload & Parsing

-   **Frontend:** `uploader.py` → calls `/upload-doc` endpoint

-   **Backend Route:** `routes/document.py`

-   **Backend Logic:**

    -   `parser.py`: Parses PDFs, DOCX, OCR with pytesseract if needed

    -   `summarizer.py`: Sends parsed text to Ollama llama 3.2 to generate summary

    -   `extractor.py`: Extracts action items using task-oriented prompt

* * * * *

### Step 2: 📧 Email Parsing

-   **Frontend:** `email_viewer.py` fetches via `/summarize-emails`

-   **Backend Route:** `routes/email.py`

-   **Logic:**

    -   `gmail_service.py`: Authenticated Gmail access, retrieves recent threads

    -   `summarizer.py`: Summarizes each email body

    -   `extractor.py`: Pulls out meetings, reminders, etc.

* * * * *

### Step 3: 🗓️ Calendar Scheduling

-   **Frontend:** `calendar_view.py` → user confirms to-do item

-   **Backend Route:** `routes/calendar.py`

-   **Logic:**

    -   `calendar_service.py`: Sends event details to Google Calendar using Calendar API

* * * * *

### Step 4: 💬 LangChain Chat Agent

-   **Frontend:** `chat_box.py`

-   **Backend Route:** `routes/chat.py`

-   **Logic:**

    -   `langchain_agent.py`: Uses LangChain's `AgentExecutor` with tools:

        -   `SummarizeDocumentTool`

        -   `ExtractTasksTool`

        -   `AddToCalendarTool`

        -   `MemoryLookupTool`

    -   `memory.py`: Maintains conversation using `ConversationBufferMemory`

* * * * *

### Step 5: 🔍 Vector Store

-   Documents are chunked and embedded using OpenAI embeddings

-   FAISS index stored in `vector_store/faiss_index.pkl`

-   Queried for document-based Q&A or follow-ups

* * * * *

🧠 LangChain Agent Architecture
-------------------------------

-   **LangChain Agent Type:** `zero-shot-react-description`

-   **Tools Registered:**

    -   `parse_document()`: Extract content from uploads

    -   `summarize(text)`: Ollama summarizer

    -   `extract_tasks(summary)`: Pull out action items

    -   `add_to_calendar(task)`: Use Google Calendar API

    -   `lookup_past_summary(question)`: FAISS + vector search

-   **Memory Type:** `ConversationBufferMemory`

* * * * *

✅ Tech Stack Summary
--------------------

| Layer | Technology |
| --- | --- |
| LLM Engine | Ollama llama 3.2 |
| Orchestration | LangChain Agents |
| Backend | FastAPI |
| Frontend | Streamlit |
| NLP Tools | OCR (Tesseract), PDFMiner, python-docx |
| Storage | MongoDB, FAISS |
| APIs | Gmail, Calendar, Drive |

* * * * *

🧪 Sample Prompts
-----------------

text

```Markdown
- "What did my boss email me last week?"
- "Summarize this PDF and schedule all meetings inside."
- "What tasks are due tomorrow?"
- "What did I do on April 15th?"
```

* * * * *

🔧 Future Features Coming Soon
-----------------------------

-   IOS app

-   Voice command input

-   WhatsApp reminders via Twilio

-   Cross-user collaboration