from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

# Define scopes
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive.metadata.readonly'
]

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES
    )
    creds = flow.run_local_server(port=8080)
    
    # Save token for reuse
    with open('token.pickle', 'wb') as token_file:
        pickle.dump(creds, token_file)
    print("✅ Token stored as token.pickle")

if __name__ == '__main__':
    main()