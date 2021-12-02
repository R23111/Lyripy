from dotenv import load_dotenv
import os

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
GENIUS_CLIENT_ACCESS_TOKEN = os.getenv('GENIUS_CLIENT_ACCESS_TOKEN')