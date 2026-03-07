import os
import json
import urllib.request

def generate_personality(top_tracks, top_genres, cluster):
    track_names = [f"{t['name']} by {t['artist']}" for t in top_tracks]

    prompt = f"""Based on someone's music taste, generate a fun and witty music personality description.

Their top tracks include: {', '.join(track_names)}
Their music cluster group is: {cluster} out of 4 personality types
Their top genres are: {', '.join(top_genres) if top_genres else 'varied/eclectic'}

Write a fun, engaging 3-4 sentence personality description that:
- Gives them a creative personality type title (e.g. "The Midnight Dreamer", "The Hype Machine")
- Describes what their music taste says about them
- Is witty and fun, like something people would want to share
- Feels personal and specific to their taste

Respond in this exact JSON format:
{{
    "title": "personality type title here",
    "description": "3-4 sentence description here",
    "emoji": "2-3 relevant emojis"
}}"""

    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    data = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    })

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            text = result["choices"][0]["message"]["content"]
            text = text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
    except Exception as e:
        print(f"GROQ ERROR: {e}")
        return {
            "title": "The Eclectic Explorer",
            "description": "Your music taste defies categorization — and that's exactly what makes it interesting. You move between moods and genres like a seasoned traveler, never staying in one place too long.",
            "emoji": "🎵✨🌍"
        }