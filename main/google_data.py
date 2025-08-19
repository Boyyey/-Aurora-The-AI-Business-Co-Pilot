# backend/google_data.py
from backend.google_oauth import get_gmail_service, get_calendar_service
from backend.memory import memory
import base64

def fetch_recent_emails(max_results=10):
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=max_results, q="in:inbox").execute()
    messages = results.get('messages', [])
    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        body = ""
        try:
            body = base64.urlsafe_b64decode(msg_data['payload']['body']['data']).decode('utf-8')
        except:
            pass
        headers = msg_data['payload']['headers']
        subject = [h['value'] for h in headers if h['name'] == 'Subject'][0]
        sender = [h['value'] for h in headers if h['name'] == 'From'][0]
        date = [h['value'] for h in headers if h['name'] == 'Date'][0]
        text = f"From: {sender}\nSubject: {subject}\nBody: {body[:200]}..."
        emails.append(text)
        memory.add(text, {"type": "email", "subject": subject, "date": date})
    return emails

def fetch_upcoming_events(max_results=10):
    service = get_calendar_service()
    events = service.events().list(calendarId='primary', maxResults=max_results, singleEvents=True,
                                   timeMin=datetime.utcnow().isoformat() + 'Z').execute()
    event_list = []
    for event in events['items']:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No title')
        event_list.append(f"Meeting: {summary} at {start}")
        memory.add(f"Meeting: {summary}", {"type": "event", "time": start})
    return event_list