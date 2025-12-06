import random
from typing import List, Dict

class StegDJBuilder:

    def __init__(self):
        pass

    def create_hour_mix(self, tracks: List[Dict], target_minutes=60) -> List[Dict]:
        """Assemble playlist close to time target"""

        mix = []
        total = 0
        
        for song in tracks:
            if total + song["duration"] <= target_minutes:
                mix.append(song)
                total += song["duration"]
            if total >= target_minutes:
                break
        
        return mix