#Author: Damien Springer
#Email: damienspringer02@gmail.com
#Description: a music downloader that downloads highest quality rip it can find & added correct meta data 

from pytube import YouTube
from pytube import Search
import logging ##To surpress warnings causes by youtube shorts 
pytube_logger = logging.getLogger('pytube')
pytube_logger.setLevel(logging.ERROR)

#Manually choose a song to download 
song = input("Enter song name")

result = Search(song)
i = 0
for x in result.results:
  print(str(i) + ": " + x.title)
  i += 1
  if (i == 5):
    break

i = int(input("Select song choice from list: "))
yt = result.results[i]
stream = yt.streams.get_audio_only()
stream.download()
