from env import *
import spotipy
from spotipy import util
import time
from track import Track
from tui import Tui

def main():     
    spotify = spotipy.Spotify(auth=util.prompt_for_user_token("R23111", "user-read-playback-state", SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, 'http://localhost:8080'))
    track = Track(spotify.current_playback())

    Tui.clear_term()

    if track == None or not track.is_playing:
        Tui.print_lyrics(title="No Track Currently Playing", lyrics="")
    else:
        Tui.print_lyrics(track.info(), track.get_lyrics())
    
    last_track = track.info()


    while(True):
        time.sleep(1)
        track = Track(spotify.current_playback())
        if track.is_playing and last_track != track.info():
            Tui.clear_term()
            Tui.print_lyrics(track.info(), track.get_lyrics())
            last_track = track.info()






    

    

    


if __name__ == "__main__":
    main()