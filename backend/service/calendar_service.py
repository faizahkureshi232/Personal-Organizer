from datetime import datetime, timedelta
from backend.service.google_auth_env import get_service
import dateutil.parser

def fetch_calendar_events():
    service = get_service('calendar', 'v3')
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now, maxResults=5,
        singleEvents=True, orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    return [e.get('summary', '(No Title)') for e in events]

def create_event(event_data: dict) -> str:
    service = get_service('calendar', 'v3')

    if 'start' not in event_data or 'dateTime' not in event_data['start']:
        raise ValueError("Event must include a start dateTime.")

    if 'end' not in event_data:
        start_dt = dateutil.parser.parse(event_data['start']['dateTime'])
        end_dt = start_dt + timedelta(hours=1)
        event_data['end'] = {
            'dateTime': end_dt.isoformat(),
            'timeZone': event_data['start'].get('timeZone', 'UTC')
        }

    ev = service.events().insert(calendarId='primary', body=event_data).execute()
    return ev.get('id')
