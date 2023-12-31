import os
import csv
import json
from datetime import date

from yt_dlp import YoutubeDL
from mutagen.mp4 import MP4
from song_metadata import SongMetadata, FIELDS

class MusicDownloader:
    CONFIG_PATH = "config.json"

    def __init__(self):
        with open(self.CONFIG_PATH, "r") as f:
            config = json.load(f)

        self.output_template = config["output_template"]
        self.output_directory = config["output_directory"]
        self.songfile_path = config["songfile_path"]
        self.ytdlp_opts = config["ytdlp_opts"]

    def _tag_song(self, path, metadata: SongMetadata):
        file = MP4(path)
        file["\xa9ART"] = metadata.artist
        file["\xa9nam"] = metadata.title
        file.save()

    def download_song(self, metadata: SongMetadata) -> int:
        self.ytdlp_opts["outtmpl"] = self.output_template.format(output_directory=self.output_directory, artist=metadata.artist, title=metadata.title)

        print(f"TEMPL: {self.ytdlp_opts['outtmpl']}")
        with YoutubeDL(self.ytdlp_opts) as ydl:
            error_code = ydl.download([metadata.url])
            if error_code == 0:
                self._tag_song(self.output_template.format(output_directory=self.output_directory, artist=metadata.artist, title=metadata.title), metadata)
                with open(self.songfile_path, "a", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=FIELDS)
                    if os.path.getsize(self.songfile_path) == 0:
                        writer.writeheader()

                    writer.writerow({
                        "artist": metadata.artist, 
                        "title": metadata.title, 
                        "date_added": metadata.date_added, 
                        "url": metadata.url
                    })

            return error_code

    def download_songfile(self):
        with open(self.songfile_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                metadata = SongMetadata(
                    artist=row["artist"],
                    title=row["title"],
                    date_added=row["date_added"],
                    url=row["url"]
                )
                self.download_song(metadata)
