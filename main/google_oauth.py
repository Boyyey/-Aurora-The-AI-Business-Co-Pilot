# backend/google_oauth.py
import pickle
import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar.readonly'
]

def authenticate():
    creds = None
    token_path = 'backend/data/token.pickle'
    credentials_path = 'credentials.json'  # Download from Google Cloud Console

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def get_gmail_service():
    creds = authenticate()
    return build('gmail', 'v1', credentials=creds)

def get_calendar_service():
    creds = authenticate()
    return build('calendar', 'v3', credentials=creds)