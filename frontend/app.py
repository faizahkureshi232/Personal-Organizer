import streamlit as st
import sys, os
# Append project root so that `backend` can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("CWD:", os.getcwd())
print("PYTHONPATH:", sys.path)

from backend.service.gmail_service import fetch_emails_summary
from backend.service.calendar_service import fetch_calendar_events, create_event
from backend.service.drive_service import fetch_drive_files
from backend.service.chat_service import answer_query

st.set_page_config(page_title="Smart Personal Organizer & Life Assistant", layout="wide")
st.title("🤖 Smart Personal Organizer & Life Assistant")

# Sidebar for Q&A
st.sidebar.header("Ask the Assistant")
user_question = st.sidebar.text_input("Your question:")
if st.sidebar.button("Ask"):
    if user_question:
        with st.spinner("Thinking..."):
            ans = answer_query(user_question)
        st.sidebar.markdown("**Assistant Response:**")
        st.sidebar.write(ans)
    else:
        st.sidebar.error("Please type a question.")

# Main Dashboard
st.header("📬 Recent Emails")
st.write(fetch_emails_summary() or "No emails.")

st.header("📆 Upcoming Events")
st.write(fetch_calendar_events() or "No events.")

st.header("📁 Drive Files")
st.write(fetch_drive_files() or "No files.")
