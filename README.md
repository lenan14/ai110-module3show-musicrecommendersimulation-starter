# 🎵 Music Recommender Simulation

## Project Summary

This project builds a simple music recommender system that suggests songs based on a user's taste profile. Songs and user preferences are represented using basic features such as genre, mood, and tempo. The system then applies a scoring method to compare songs with the user's preferences and rank them accordingly. While it is a simplified version, it reflects how platforms like Spotify personalize recommendations. The project also explores how well the system performs, what it gets right or wrong, and how these ideas connect to real-world AI recommendation systems.

---

## How The System Works

This music recommender is designed to mimic how real streaming platforms like Spotify suggest songs to their users. In real systems, recommendations are based on a combination of collaborative filtering, which looks at what people with similar tastes enjoy, and content-based filtering, which focuses on song features like genre, tempo, and mood. For this version, the system will focus more on matching song characteristics to user preferences while still taking general listening patterns into account. The goal is to create recommendations that feel personal and relevant, even though the system is simpler than those used by large streaming platforms.

My version uses content-based filtering with a weighted scoring system:

**Features Used:**
- Genre (pop, rock, lofi, jazz, etc.)
- Mood (happy, chill, intense, relaxed, etc.) 
- Energy level (0.0-1.0 scale, where higher = more energetic)
- Acousticness (0.0-1.0 scale, where higher = more acoustic)

**User Profile:**
The system expects user preferences as a dictionary with:
- `genre`: favorite genre (string)
- `mood`: favorite mood (string)  
- `energy`: target energy level (0.0-1.0 float)

**Scoring Logic:**
- +2.0 points for exact genre match
- +1.0 point for exact mood match
- Energy similarity score: 1.0 - |song_energy - user_target_energy| (ranges 0.0-1.0)

Songs are ranked by total score (highest first) and the top recommendations are returned with explanations of why each song was recommended.

**Algorithm Recipe:**
1. Take the user's taste profile, including their preferred genre, mood, and energy level.  
2. Loop through each song in the dataset.  
3. For each song, compare its features (genre, mood, energy) to the user's preferences.  
4. Assign a score:
   - Add 2.0 points if the genre matches  
   - Add 1.0 point if the mood matches  
   - Add an energy similarity score based on how close the song's energy is to the user's target  
5. Calculate the total score for each song.  
6. Sort all songs from highest to lowest score.  
7. Return the top-ranked songs as recommendations with explanations.

**Potential Biases:**
- This system may over-prioritize genre because it has the highest weight, which could cause it to ignore songs that better match the user's mood or energy but belong to a different genre.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
py -m src.main
# or if you have python on PATH:
# python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

I tested the system with four different user profiles to evaluate its performance:

1. **Pop Happy High Energy** (genre: pop, mood: happy, energy: 0.8)
   - Top result: Sunrise City (pop/happy/0.82) - perfect match with score 3.98
   - Shows the system correctly prioritizes exact matches

2. **Chill Lofi Low Energy** (genre: lofi, mood: chill, energy: 0.4)  
   - Top results: Focus Flow (lofi/focused/0.40) and Library Rain (lofi/chill/0.35)
   - Demonstrates energy similarity scoring works for lower energy preferences

3. **Intense Rock High Energy** (genre: rock, mood: intense, energy: 0.9)
   - Top result: Storm Runner (rock/intense/0.91) - exact match
   - Followed by Metal Thunder (metal/intense/0.98) - mood and energy match but different genre

4. **Relaxed Jazz Medium Energy** (genre: jazz, mood: relaxed, energy: 0.5)
   - Top result: Coffee Shop Stories (jazz/relaxed/0.37) - perfect genre/mood match
   - Shows the system can find good matches even with energy differences

**Key Findings:**
- Genre matches (+2.0 points) have strong influence on rankings
- The system successfully differentiates between energy levels
- Mood matches (+1.0) provide good secondary ranking
- Energy similarity scoring (0-1.0) works well for fine-tuning recommendations

## CLI Verification + Recommendation Screenshot
![Terminal Output 8](src/screenshots/Screenshot%202026-04-03%20151529.png)

## Stress Test with Diverse Profiles Screenshots
Here are screenshots of the terminal's output for each profile's recommendations:

![Terminal Output 1](src/screenshots/Screenshot%202026-04-03%20143731.png)
![Terminal Output 2](src/screenshots/Screenshot%202026-04-03%20143747.png)
![Terminal Output 3](src/screenshots/Screenshot%202026-04-03%20143755.png)
![Terminal Output 4](src/screenshots/Screenshot%202026-04-03%20143807.png)
![Terminal Output 5](src/screenshots/Screenshot%202026-04-03%20143817.png)
![Terminal Output 6](src/screenshots/Screenshot%202026-04-03%20143845.png)
![Terminal Output 7](src/screenshots/Screenshot%202026-04-03%20143852.png)

These screenshots show the formatted recommendations with scores, reasons, and song details for different user profiles.

---

## Limitations and Risks

My recommender system has some clear limitations that make it less effective than real music platforms. The dataset is really small with only 19 songs, so it can't offer much variety or discover new music for users. It only looks at basic features like genre and mood, completely ignoring things like lyrics, artist popularity, or how songs sound together in a playlist. The scoring system heavily favors genre matches, which means users who like pop music will mostly get pop recommendations even if they want something different. This creates a filter bubble where people might miss out on great songs from other genres that match their mood or energy level perfectly.

---

## Reflection

This project taught me how recommendation systems balance different types of user preferences. My biggest learning moment was realizing how simple weighted scoring can create effective recommendations, but also how those weights can create unintended biases.

AI tools (GitHub Copilot) were incredibly helpful for brainstorming the scoring logic and generating diverse test songs, but I had to double-check the math to ensure the energy similarity calculation was correct.

The most surprising discovery was how well the system worked despite its simplicity - it successfully differentiated between "intense rock" and "chill lofi" profiles, showing that even basic content-based filtering can feel intelligent.

For the next iteration, I'd experiment with non-linear energy scoring and add collaborative filtering to reduce genre bias.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

VibeFinder is designed to recommend songs to users based on their musical preferences. It takes a user's favorite genre, preferred mood, and target energy level, then suggests the top 5 most relevant songs from a catalog. This simulation demonstrates how content-based music recommendation systems work, helping users discover songs that match their current vibe.

The system is intended for educational purposes and personal music discovery, not for production use in real music streaming platforms.

---

## 3. How It Works (Short Explanation)

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

---

## 9. Personal Reflection

Building VibeFinder taught me how even a simple weighted scoring system can produce meaningful recommendations. I was surprised by how well the system differentiated between distinct user profiles like “intense rock” versus “chill lofi,” showing that even small datasets can illustrate recommendation concepts. Using AI tools helped speed up creating diverse test songs and brainstorming scoring logic, but I learned that human judgment is still crucial to verify calculations and ensure the recommendations feel reasonable. In future iterations, I want to explore balancing weights and adding collaborative filtering to reduce bias and make the system feel more dynamic.