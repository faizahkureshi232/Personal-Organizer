import os
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

load_dotenv()

SCOPES = {
    'gmail': ['https://www.googleapis.com/auth/gmail.readonly'],
    'calendar': ['https://www.googleapis.com/auth/calendar'],
    'drive': ['https://www.googleapis.com/auth/drive.metadata.readonly'],
}

def get_service(api_name: str, version: str = 'v1'):
    creds = Credentials(
        token=None,
        refresh_token=os.getenv("GOOGLE_REFRESH_TOKEN"),
        token_uri=os.getenv("GOOGLE_TOKEN_URI", "https://oauth2.googleapis.com/token"),
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        scopes=SCOPES.get(api_name, []),
    )
    return build(api_name, version, credentials=creds)
