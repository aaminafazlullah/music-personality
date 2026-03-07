from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import spotipy
from spotify import create_spotify_oauth, get_user_top_tracks, get_user_top_artists
from ml_model import get_personality_cluster
from personality import generate_personality
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Music Personality API is running!"}

@app.get("/login")
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return RedirectResponse(url=auth_url)

@app.get("/callback")
def callback(code: str):
    sp_oauth = create_spotify_oauth()
    token_info = sp_oauth.get_access_token(code)
    sp = spotipy.Spotify(auth=token_info["access_token"])

    tracks = get_user_top_tracks(sp)
    artists = get_user_top_artists(sp)

    cluster, n_clusters, top_genres = get_personality_cluster(artists)
    personality = generate_personality(tracks[:5], top_genres, cluster)

    return {
        "top_tracks": tracks[:5],
        "top_genres": top_genres,
        "personality": personality
    }