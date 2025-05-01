from fastapi import FastAPI
from routes import document, email, calendar, chat

app = FastAPI()
app.include_router(document.router)
app.include_router(email.router)
app.include_router(calendar.router)
app.include_router(chat.router)