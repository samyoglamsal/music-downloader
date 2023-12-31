from datetime import date

from flask import Flask, request, Response
from flask_cors import CORS
from music_downloader import MusicDownloader
from song_metadata import SongMetadata

music_downloader = MusicDownloader()
app = Flask(__name__)
CORS(app)

@app.route("/download-song", methods=["POST"])
def download_song():
    metadata = SongMetadata(
        artist=request.json["artist"],
        title=request.json["title"],
        date_added=date.today().isoformat(),
        url=request.json["url"]
    )
    
    if music_downloader.download_song(metadata) == 0:
        return Response("Success", 200)
    else:
        return Response("Error: Unable to download the song.", 500)