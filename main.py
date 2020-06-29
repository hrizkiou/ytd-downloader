from playlist import Plist
from video import video
import sys



while True:
    isVidOrPlay = input('Do you need to download a playlist or Video: ').lower()


    if isVidOrPlay == 'pl':
        url = input('Enter the playlist URL: ')
        Plist(url)
        
    elif isVidOrPlay == 'vi':
        url = input('Enter the video URL: ')
        video(url)
    else:
        print('please enter video or playlist')
        continue
    repeat = input('Do you need to download an other Video or Playlist [enter Y for yes or N for No]: ').lower()

   
    x = 1
    while repeat != 'y' and repeat != 'n' and x <= 3:
        repeat = input("please enter 'Y' or 'N': ").lower()
        if x == 3:
            print('Sorry.. Invalide enter')
            sys.exit()
        x += 1
    if repeat == 'y':
        continue
    elif repeat == 'n':
        break
    