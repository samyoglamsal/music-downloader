import json

from mutagen.mp4 import MP4 
from flask import Flask, request, Response
from flask_cors import CORS
from yt_dlp import YoutubeDL

OUTPUT_DIR = "/mnt/c/Users/samyo/Desktop/songs"

app = Flask(__name__)
CORS(app)

@app.route("/download-song", methods=["POST"])
def download_song():
    artist = request.json["artist"]
    title = request.json["title"]
    url = request.json["url"]

    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "postprocessors": [{  # Extract audio using ffmpeg
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a",
        }],
        "outtmpl": f"{OUTPUT_DIR}/{artist} - {title}.m4a"
    }
    with YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download([url])

        if error_code == 0:
            tag_song(f"{OUTPUT_DIR}/{artist} - {title}.m4a", request.json)
        else:
            return Response("Error: Unable to download the song.", 500)

    return Response("Success", 200)

def tag_song(path, tags):
    file = MP4(path)
    file["\xa9ART"] = tags["artist"]
    file["\xa9nam"] = tags["title"]
    file.save()

