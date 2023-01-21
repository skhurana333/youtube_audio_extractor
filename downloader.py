#!/usr/bin/python

from __future__ import unicode_literals
import youtube_dl  # pip install youtube_dl
import sys
import os


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'progress_hooks': [my_hook],
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def main():
    if len(sys.argv) < 3 :
        print("python downloadey.py file_having_youtube_urls output_path")
        exit(0)

    file = sys.argv[1]
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    print("getting from file:" + file)
    with open(file, 'r') as input :
        for line in input :
            print("downloading line : " + line)
            downloaded = ydl.download([line])
            info_dict = ydl.extract_info(line, download=False)

            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            print("video_id:" + video_id + "video_title:" +video_title)
            downloadedfilename = "'" + video_title + "-" +video_id + "'*"
            print("cp " + downloadedfilename + " "  + sys.argv[2] + "/")
            os.system( "cp " + downloadedfilename + " "  + sys.argv[2] + "/"  )


main()
