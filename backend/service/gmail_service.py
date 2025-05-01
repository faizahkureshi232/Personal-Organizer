
''' This mock version and does not yet connect to the actual Gmail API.
 In a real implementation, you would need to integrate Google OAuth 2.0 authentication to securely access a user's Gmail inbox.

To complete this:

Set up a Google Cloud Project.

Enable the Gmail API and generate OAuth 2.0 credentials.

Use libraries like google-auth, google-api-python-client, and google-auth-oauthlib to handle login, token refresh, and API calls.

Replace the mock function with actual code that fetches emails using the Gmail API.
'''



'''
the above steps are done 
'''
from googleapiclient.discovery import build
from backend.service.google_auth_env import get_service

def fetch_emails_summary():
    service = get_service('gmail')
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    emails = results.get('messages', [])
    subjects = []
    for msg in emails:
        data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name']=='Subject'), '(No Subject)')
        subjects.append(subject)
    return subjects

# Additional Gmail API functionalities can be added similarly
