import os
from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = os.environ.get('YOUTUBE_API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search(q, max_results):
    api = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = api.search().list(
        q=q,
        part="id,snippet",
        maxResults=max_results
    ).execute()
    return search_response.get("items", [])
