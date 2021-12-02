from env import *
import spotipy
from spotipy import util

from track import Track


def main(): 
    spotify = spotipy.Spotify(auth=util.prompt_for_user_token("R23111", "user-read-playback-state", SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, 'http://localhost:8080'))

    track = Track(spotify.current_playback())

    print(track.get_lyrics())

    


if __name__ == "__main__":
    main()