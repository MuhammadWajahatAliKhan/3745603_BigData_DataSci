from googleapiclient.discovery import build
import json

API_KEY = 'AIzaSyDi3QhcT6ayP5ExQwY5p0nnY8g4iSVglnU'

youtube = build('youtube', 'v3', developerKey=API_KEY)

channel_id = 'UCMiJRAwDNSNzuYeN2uWa0pA'

video_fields = 'snippet, statistics'

playlist_fields = 'snippet'

videos_response = youtube.search().list(
    channelId=channel_id,
    part='id',
    order='date',
    type='video',
    maxResults=50
).execute()

video_ids = [item['id']['videoId'] for item in videos_response['items']]

videos_response = youtube.videos().list(
    id=','.join(video_ids),
    part=video_fields
).execute()

playlists_response = youtube.playlists().list(
    channelId=channel_id,
    part='id',
    maxResults=50
).execute()

playlist_ids = [item['id'] for item in playlists_response['items']]

playlists_response = youtube.playlists().list(
    id=','.join(playlist_ids),
    part=playlist_fields
).execute()

vids = json.dumps (videos_response)
with open('vids.txt', 'w') as f:
    f.write(vids)

playlist = json.dumps (playlists_response)
with open('playlist.txt', 'w') as f:
    f.write(playlist)
