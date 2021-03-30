from pydub import AudioSegment
import os

song = AudioSegment.from_mp3(os.getcwd()+"/Sarkodie - Adonai ft. Castro (Official Video)-ipZvlG-wwWk.mp3")


def range_inc(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


thirty_secs = list(range_inc(0, len(song), 30000))
thirty_secs.append(len(song))
parts = []
for x in range(len(thirty_secs)-1):
    parts.append(song[thirty_secs[x]:thirty_secs[x+1]])

'''

from __future__ import unicode_literals
import youtube_dl
import os
import uuid


temp_path = str(uuid.uuid4())
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': temp_path+'/song.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=ipZvlG-wwWk'])
'''