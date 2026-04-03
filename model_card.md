# 🎧 Model Card: VibeFinder 1.0

## 1. Model Name  

VibeFinder 1.0

---

## 2. Intended Use  

VibeFinder is designed to recommend songs to users based on their musical preferences. It takes a user's favorite genre, preferred mood, and target energy level, then suggests the top 5 most relevant songs from a catalog. This simulation demonstrates how content-based music recommendation systems work, helping users discover songs that match their current vibe.

The system is intended for educational purposes and personal music discovery, not for production use in real music streaming platforms.

---

## 3. How the Model Works  

VibeFinder uses a simple weighted scoring system to match songs to user preferences:

**Features Used:**
- Genre (categorical: pop, rock, lofi, jazz, electronic, etc.)
- Mood (categorical: happy, chill, intense, relaxed, moody, etc.)  
- Energy level (numerical: 0.0-1.0, where higher = more energetic)

**Scoring Rules:**
- +2.0 points for exact genre match
- +1.0 point for exact mood match
- Energy similarity: 1.0 - |song_energy - user_target_energy| (0.0-1.0 scale)

Total score = genre_points + mood_points + energy_similarity

Songs are ranked by total score (highest first) and explanations are provided showing which criteria matched.

---

## 4. Data  

**Dataset Size:** 19 songs in the catalog

**Genres Represented:** pop, rock, lofi, jazz, synthwave, indie pop, electronic, country, classical, hip hop, ambient, reggae, metal, folk

**Moods Represented:** happy, chill, intense, relaxed, moody, focused

**Data Sources:** Manually created diverse song catalog with realistic attributes

**Limitations:** Small dataset may not represent all musical tastes. Lacks real user listening data and collaborative filtering.

---

## 5. Strengths

VibeFinder works well for users with clear genre and mood preferences. It successfully differentiates between high-energy vs. low-energy music preferences and provides transparent explanations for recommendations. The weighted scoring system allows for nuanced matching that goes beyond simple categorical matching.

---

## 6. Limitations and Bias 

**Primary Limitation:** The system over-prioritizes genre matches (2.0 points) compared to mood (1.0 point), which can create "filter bubbles" where users only get recommendations from their favorite genre even if other genres might match their mood perfectly.

**Dataset Bias:** The current catalog has more pop and electronic songs, which may bias recommendations toward these genres.

**Feature Limitations:** Doesn't consider tempo, danceability, valence, or acousticness in the main scoring (though these are available in the data). Real systems would use more sophisticated algorithms.

**User Experience Issue:** The energy similarity scoring might not be intuitive - a song with energy 0.3 getting a 0.7 similarity score for a user wanting energy 1.0 may not feel like a good match to users.

---

## 7. Evaluation  

I tested VibeFinder with four distinct user profiles:

1. **Pop Happy High Energy** - Perfect matches scored 3.98/4.0, showing strong performance for clear preferences
2. **Chill Lofi Low Energy** - Successfully found chill songs with appropriate energy levels  
3. **Intense Rock High Energy** - Prioritized exact genre/mood matches but also found high-energy alternatives
4. **Relaxed Jazz Medium Energy** - Found the single jazz song despite energy differences

The system performed well for users with strong genre preferences but showed limitations when genre matches were scarce. Energy similarity worked as expected, and explanations helped understand the scoring logic.

---

## 8. Future Work  

- **Add More Features:** Incorporate danceability, valence, and tempo into scoring
- **Improve Energy Scoring:** Use a non-linear similarity function for more intuitive energy matching
- **Balance Weights:** Experiment with different weightings for genre vs. mood vs. energy
- **Expand Dataset:** Add hundreds of songs for better diversity and testing
- **Collaborative Features:** Add user-user similarity or song-song similarity
- **Better Explanations:** Show how close misses performed and why they were ranked lower

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
