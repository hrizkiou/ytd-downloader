import youtube_dl
import sys

class video():
    def __init__(self, url):
        ydl_options = {
            'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist':True,
        }
        with youtube_dl.YoutubeDL(ydl_options) as vdl:
            vdl.download([url])
