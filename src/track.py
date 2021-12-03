import lyricsgenius
from env import *

class Track:
    def __init__(self, playback) -> None:
        self.__album = playback["item"]["album"]["name"]
        self.__title = playback["item"]["name"]
        self.__artist = playback["item"]["artists"][0]["name"]
        

    def print_info(self) -> str:
        return f"{self.__title} by {self.__artist} from {self.__album}"

    def get_lyrics(self, mode=None) -> str:
        genius = lyricsgenius.Genius(GENIUS_CLIENT_ACCESS_TOKEN)
        genius.response_format = "html"
        genius.verbose = False
        genius.remove_section_headers = True
        genius_search = genius.search_song(title=self.__title, artist=self.__artist, get_full_info=False).lyrics


        if(genius_search != None):
            f = open("lyrics.md", "w")
            f.write(genius_search.replace("\n", "\n\n"))
            f.close()
            return genius_search
        return ""