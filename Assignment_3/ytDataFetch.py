from googleapiclient.discovery import build
from pymongo import MongoClient

api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey='AIzaSyDi3QhcT6ayP5ExQwY5p0nnY8g4iSVglnU')

client = MongoClient("mongodb://localhost:27017/")
db = client["youtube"]


#Retrieve the most popular videos in a specific category in the past week 
collectionMostPopularinCategory = db["popular_videos_in_category"]

request = youtube.videos().list(
    part="snippet",
    chart="mostPopular",
    videoCategoryId="17", 
    maxResults=10,
)
response = request.execute()

for item in response["items"]:
    video_data = {
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"],
        "publishedAt": item["snippet"]["publishedAt"],
        "categoryId": item["snippet"]["categoryId"],
    }
    collectionMostPopularinCategory.insert_one(video_data)



#videos that match a specific keyword and are longer than 20 minutes
collectionLongVideos = db["long_videos"]

request = youtube.search().list(
    part="snippet",
    q="cats",
    type="video",
    videoDuration="long",
    maxResults=10
)
response = request.execute()

for item in response["items"]:
    video_data = {
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"],
        "publishedAt": item["snippet"]["publishedAt"],
        "channelId": item["snippet"]["channelId"],
    }
    collectionLongVideos.insert_one(video_data)



#Retrieve the latest comments on a specific video

collectionLatestComment = db["latest_comments"]

request = youtube.commentThreads().list(
    part="snippet",
    videoId="jNQXAC9IVRw",
    order="time",
    maxResults=10
)
response = request.execute()

for item in response["items"]:
    comment_data = {
        "commentText": item["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
        "authorName": item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
        "publishedAt": item["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
        "likeCount": item["snippet"]["topLevelComment"]["snippet"]["likeCount"],
        "videoId": item["snippet"]["topLevelComment"]["snippet"]["videoId"]
    }
    collectionLatestComment.insert_one(comment_data)


#Retrieve the details of a specific playlist

collectionPlaylist = db["playlist_details"]

request = youtube.playlists().list(
    part="snippet",
    id="PLRNsqJKPXrnkNM24Pd3N720RqbQ67FpML" 
)
response = request.execute()

for item in response["items"]:
    playlist_data = {
        "playlistId": item["id"],
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"],
        "publishedAt": item["snippet"]["publishedAt"]
    }
    collectionPlaylist.insert_one(playlist_data)