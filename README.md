# 🎵 Music Recommender Simulation

## Project Summary

This project builds a simple music recommender system that suggests songs based on a user’s taste profile. Songs and user preferences are represented using basic features such as genre, mood, and tempo. The system then applies a scoring method to compare songs with the user’s preferences and rank them accordingly. While it is a simplified version, it reflects how platforms like Spotify personalize recommendations. The project also explores how well the system performs, what it gets right or wrong, and how these ideas connect to real-world AI recommendation systems.

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
1. Take the user’s taste profile, including their preferred genre, mood, and energy level.  
2. Loop through each song in the dataset.  
3. For each song, compare its features (genre, mood, energy) to the user’s preferences.  
4. Assign a score:
   - Add 2.0 points if the genre matches  
   - Add 1.0 point if the mood matches  
   - Add an energy similarity score based on how close the song’s energy is to the user’s target  
5. Calculate the total score for each song.  
6. Sort all songs from highest to lowest score.  
7. Return the top-ranked songs as recommendations with explanations.

**Potential Biases**
- This system may over-prioritize genre because it has the highest weight, which could cause it to ignore songs that better match the user’s mood or energy but belong to a different genre.
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
python -m src.main
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

## CLI Verification Screenshot

Here is the terminal output showing recommendations for the default "pop/happy" profile:

```
Loading songs from ../data/songs.csv...
Loaded songs: 19

=== Pop Happy High Energy ===
1. Sunrise City by Neon Echo - Score: 3.98
   Because: genre match (+2.0), mood match (+1.0), energy similarity (0.98)
   Genre: pop, Mood: happy, Energy: 0.82
2. Gym Hero by Max Pulse - Score: 2.87
   Because: genre match (+2.0), energy similarity (0.87)
   Genre: pop, Mood: intense, Energy: 0.93
3. Rooftop Lights by Indigo Parade - Score: 1.96
   Because: mood match (+1.0), energy similarity (0.96)
   Genre: indie pop, Mood: happy, Energy: 0.76
4. Dance Fever by Electro Beats - Score: 1.88
   Because: mood match (+1.0), energy similarity (0.88)
   Genre: electronic, Mood: happy, Energy: 0.92
5. Night Drive Loop by Neon Echo - Score: 0.95
   Because: energy similarity (0.95)
   Genre: synthwave, Mood: moody, Energy: 0.75
```

The output shows clean, readable formatting with song titles, scores, scoring reasons, and song attributes for each recommendation.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

This project taught me how recommendation systems balance different types of user preferences. My biggest learning moment was realizing how simple weighted scoring can create effective recommendations, but also how those weights can create unintended biases.

AI tools (GitHub Copilot) were incredibly helpful for brainstorming the scoring logic and generating diverse test songs, but I had to double-check the math to ensure the energy similarity calculation was correct.

The most surprising discovery was how well the system worked despite its simplicity - it successfully differentiated between "intense rock" and "chill lofi" profiles, showing that even basic content-based filtering can feel intelligent.

For the next iteration, I'd experiment with non-linear energy scoring and add collaborative filtering to reduce genre bias.

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

