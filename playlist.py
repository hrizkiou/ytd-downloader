import youtube_dl
import sys
import os

class Plist():
    def __init__(self, url):
        ydl_opts = {
            'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
            'outtmpl': '%(playlist)s/%(playlist_index)s __%(title)s.%(ext)s',
            # 'subtitleslangs': ['en'],
            # 'writeautomaticsub': True,
            'yesplaylist':True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as pdl:
            pdl.download([url])