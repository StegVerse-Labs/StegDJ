from fastapi import FastAPI
import json
from core.selector import StegDJSelector
from core.builder import StegDJBuilder

app = FastAPI()
with open("data/library.json") as f:
    library = json.load(f)

@app.post("/mix")
def generate_mix(styles: list, mood: str = None, minutes: int = 60):
    selector = StegDJSelector(library)
    builder = StegDJBuilder()

    pool = selector.get_tracks(styles=styles, mood=mood)
    playlist = builder.create_hour_mix(pool, target_minutes=minutes)

    return {
        "songs": playlist,
        "duration": sum(s["duration"] for s in playlist),
        "count": len(playlist)
    }