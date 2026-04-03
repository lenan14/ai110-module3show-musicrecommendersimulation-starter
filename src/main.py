"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
import sys

# Ensure this module can be run both as a script and as a package (python -m src.main)
base_dir = os.path.dirname(os.path.abspath(__file__))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from recommender import load_songs, recommend_songs

def main() -> None:
    songs_path = os.path.join(base_dir, "..", "data", "songs.csv")
    songs = load_songs(songs_path)

    # Test different user profiles
    profiles = [
        {"name": "Pop Happy High Energy", "prefs": {"genre": "pop", "mood": "happy", "energy": 0.8}},
        {"name": "Chill Lofi Low Energy", "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.4}},
        {"name": "Intense Rock High Energy", "prefs": {"genre": "rock", "mood": "intense", "energy": 0.9}},
        {"name": "Relaxed Jazz Medium Energy", "prefs": {"genre": "jazz", "mood": "relaxed", "energy": 0.5}},
    ]

    for profile in profiles:
        print(f"\n=== {profile['name']} ===")
        print("{:<3} {:<35} {:<7} {}".format("#", "Title", "Score", "Reasons"))
        print("-" * 90)

        recommendations = recommend_songs(profile['prefs'], songs, k=5)

        for i, (song, score, explanation) in enumerate(recommendations, 1):
            print("{:<3} {:<35} {:<7.2f} {}".format(i, song['title'], score, explanation))
            print(f"     Artist: {song['artist']} | Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']:.2f}")
            print("     " + "-" * 80)

        print()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()