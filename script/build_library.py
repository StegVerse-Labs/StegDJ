import librosa
import json
from pathlib import Path

def analyze_audio(filepath: str) -> dict:
    y, sr = librosa.load(filepath, duration=90)  # sample first 90 seconds
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    duration = librosa.get_duration(y=y, sr=sr) / 60

    # crude mood inference
    mood = "energetic" if tempo > 115 else "chill"

    return {
        "file": filepath,
        "tempo": round(float(tempo)),
        "duration": round(duration, 2),
        "moods": [mood, "any"]
    }

def scan_library(mp3_folder="music_import/"):
    songs = []
    for file in Path(mp3_folder).glob("*.mp3"):
        meta = analyze_audio(str(file))
        # style must be assigned once (country/edm/etc)
        # or auto-detected with tags in v2
        meta["style"] = "unknown"
        songs.append(meta)

    with open("data/library.json", "w") as f:
        json.dump({"songs": songs}, f, indent=2)

if __name__ == "__main__":
    scan_library()
