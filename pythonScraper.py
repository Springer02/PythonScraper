#Author: Damien Springer
#Email: damienspringer02@gmail.com
#Description: a music downloader that downloads highest quality rip it can find & added correct meta data 

from pytube import YouTube
from pytube import Search
import logging ##To surpress warnings causes by youtube shorts 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pytube_logger = logging.getLogger('pytube')
pytube_logger.setLevel(logging.ERROR)

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def main():
  while True:
    print("Options:")
    print("1: Search for Single Song")
    print("quit: Exit the Program")
    userinput = input("User Choice: ")
    if (userinput == "1"):
      manuallyYoutubeSongSearch()
    if (userinput == "quit"):
      break

 
#Manually choose a song to download 
def manuallyYoutubeSongSearch():
  while True:
    song = input("Enter song name artist name")
    result = Search(song)
    i = 0
    for x in result.results:
      print(str(i) + ": " + x.title)
      i += 1
      if (i == 5):
        break

    i = input("Select song choice from list (or back to search a new song): ")
    if (i != "back"):
      yt = result.results[int(i)]
      stream = yt.streams.get_audio_only()
      stream.download()
      break

def searchSong():
  print("Options:")

def searchArtist():
  print("Options:")


def searchAlbumArtist():
  print("Options:")

  
#download song with metadata 
def downloadSong():
  print("Options:")

if __name__ == "__main__":
  main()
