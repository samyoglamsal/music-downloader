import os
import io
import mutagen

from flask import Flask, request
from flask_cors import CORS
from yt_dlp import YoutubeDL

OUTPUT_DIR = "/mnt/c/Users/samyo/Desktop/songs"

app = Flask(__name__)
CORS(app)

@app.route("/download-song", methods=["POST"])
def download_song():
    artist = request.json["artist"]
    title = request.json["title"]
    date_added = request.json["date_added"]
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

    return {"status": 200}

def tag_song(song):
    pass