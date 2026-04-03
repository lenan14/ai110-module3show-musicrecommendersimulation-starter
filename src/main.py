"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Test different user profiles
    profiles = [
        {"name": "Pop Happy High Energy", "prefs": {"genre": "pop", "mood": "happy", "energy": 0.8}},
        {"name": "Chill Lofi Low Energy", "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.4}},
        {"name": "Intense Rock High Energy", "prefs": {"genre": "rock", "mood": "intense", "energy": 0.9}},
        {"name": "Relaxed Jazz Medium Energy", "prefs": {"genre": "jazz", "mood": "relaxed", "energy": 0.5}},
    ]

    for profile in profiles:
        print(f"\n=== {profile['name']} ===")
        recommendations = recommend_songs(profile['prefs'], songs, k=5)
        
        for i, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"{i}. {song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"   Because: {explanation}")
            print(f"   Genre: {song['genre']}, Mood: {song['mood']}, Energy: {song['energy']}")
        print()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
