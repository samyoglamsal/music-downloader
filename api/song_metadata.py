from dataclasses import dataclass

FIELDS = ["artist", "title", "date_added", "url"]

@dataclass
class SongMetadata:
    artist: str
    title: str
    date_added: str
    url: str