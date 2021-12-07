import lyricsgenius
from env import *

class Track:
    def __init__(self, playback) -> None:
        if playback == None:
            self.__album = ""
            self.__title = ""
            self.__artist = ""
            self.is_playing = False
        else:
            self.__album = playback["item"]["album"]["name"]
            self.__title = playback["item"]["name"]
            self.__artist = playback["item"]["artists"][0]["name"]
            self.is_playing = playback["is_playing"]
        

    def info(self) -> str:
        return f"{self.__title} by {self.__artist}"

    def get_lyrics(self, mode=None) -> str:
        genius = lyricsgenius.Genius(GENIUS_CLIENT_ACCESS_TOKEN)
        genius.response_format = "html"
        genius.verbose = False
        genius.remove_section_headers = True
        genius_search = genius.search_song(title=self.__title, artist=self.__artist, get_full_info=False)


        if(genius_search != None):
            return genius_search.lyrics
        return ""