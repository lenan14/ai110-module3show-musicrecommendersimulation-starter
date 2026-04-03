from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Recommend top k songs for a user based on their profile."""
        scored_songs = []
        for song in self.songs:
            score = self._calculate_score(user, song)
            scored_songs.append((song, score))
        
        # Sort by score (highest first)
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was recommended for a user."""
        
        if song.genre == user.favorite_genre:
            reasons.append("genre match")
        
        if song.mood == user.favorite_mood:
            reasons.append("mood match")
        
        energy_diff = abs(song.energy - user.target_energy)
        energy_score = 1.0 - energy_diff
        reasons.append(f"energy similarity ({energy_score:.2f})")
        
        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append("acoustic preference")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("non-acoustic preference")
        
        return ", ".join(reasons)
    
    def _calculate_score(self, user: UserProfile, song: Song) -> float:
        """Calculate score for a song based on user preferences."""
        score = 0.0
        
        # Genre match (+2.0)
        if song.genre == user.favorite_genre:
            score += 2.0
        
        # Mood match (+1.0)
        if song.mood == user.favorite_mood:
            score += 1.0
        
        # Energy similarity
        energy_diff = abs(song.energy - user.target_energy)
        score += 1.0 - energy_diff
        
        # Acoustic preference
        if user.likes_acoustic:
            score += song.acousticness
        else:
            score += (1.0 - song.acousticness)
        
        return score

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return as list of dictionaries."""
    songs = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numerical values to appropriate types
            song_dict = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song_dict)
    print(f"Loading songs from {csv_path}...")
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Score a song based on user preferences and return score with explanation."""
    score = 0.0
    reasons = []
    
    # Genre match
    if song['genre'] == user_prefs.get('genre', ''):
        score += 2.0
        reasons.append("genre match (+2.0)")
    
    # Mood match
    if song['mood'] == user_prefs.get('mood', ''):
        score += 1.0
        reasons.append("mood match (+1.0)")
    
    # Energy similarity (closer to target = higher score)
    target_energy = user_prefs.get('energy', 0.5)
    energy_diff = abs(song['energy'] - target_energy)
    energy_score = 1.0 - energy_diff  # This gives 1.0 for perfect match, 0.0 for max difference
    score += energy_score
    reasons.append(f"energy similarity ({energy_score:.2f})")
    
    explanation = ", ".join(reasons)
    return score, explanation

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Recommend top k songs based on user preferences with scores and explanations."""
    # Score all songs
    scored_songs = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored_songs.append((song, score, explanation))
    
    # Sort by score (highest first) and return top k
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    return scored_songs[:k]