import lyricsgenius
from env import *

class Track:
    def __init__(self, playback) -> None:
        self.__album = playback["item"]["album"]["name"]
        self.__title = playback["item"]["name"]
        self.__artist = playback["item"]["artists"][0]["name"]
        

    def print_info(self) -> str:
        return f"{self.__title} by {self.__artist} from {self.__album}"

    def get_lyrics(self, mode=None):
        genius = lyricsgenius.Genius(GENIUS_CLIENT_ACCESS_TOKEN)
        genius.verbose = False
        genius.remove_section_headers = True

        genius_search = genius.search_song(title=self.__title, artist=self.__artist, get_full_info=False)

        if(genius_search != None):
            return genius_search.lyrics