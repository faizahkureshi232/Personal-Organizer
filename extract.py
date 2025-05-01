# extract_refresh_token.py
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



with open("token.pickle", "rb") as token_file:
    creds = pickle.load(token_file)
    print("Refresh Token:", creds.refresh_token)
