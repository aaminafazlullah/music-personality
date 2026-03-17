import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("REDIRECT_URI"),
        scope="user-top-read user-read-recently-played",
        cache_handler=spotipy.cache_handler.MemoryCacheHandler()
    )

def get_user_top_tracks(sp):
    results = sp.current_user_top_tracks(limit=50, time_range="medium_term")
    tracks = []
    for track in results["items"]:
        tracks.append({
            "id": track["id"],
            "name": track["name"],
            "artist": track["artists"][0]["name"]
        })
    return tracks

def get_user_top_artists(sp):
    results = sp.current_user_top_artists(limit=50, time_range="medium_term")
    artists = []
    for artist in results["items"]:
        artists.append({
            "name": artist["name"],
            "genres": artist.get("genres", []),
            "popularity": artist.get("popularity", 0)
        })
    return artists