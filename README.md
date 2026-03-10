# 🎵 Music Personality

> Discover what your music taste says about your soul.

A full-stack AI/ML web app that analyzes your Spotify listening history, clusters your music taste using machine learning, and generates a witty personalized personality description using an LLM.

## ✨ Features

- **Spotify OAuth** — securely connects to your account
- **ML Clustering** — K-Means algorithm groups your listening patterns into personality types
- **LLM Generation** — LLaMA 3.3 70B generates a personalized, witty personality description
- **Retro UI** — vinyl-inspired design with grain texture, particles, and custom cursor
- **Shareable** — copy your personality to share with friends

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| Auth | Spotify OAuth via Spotipy |
| ML | scikit-learn, K-Means clustering |
| LLM | Groq API (LLaMA 3.3 70B) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Docker, AWS EC2 (Ubuntu) |

## 🚀 Running Locally

1. Clone the repo
```bash
git clone https://github.com/aaminafazlullah/music-personality.git
cd music-personality
```

2. Set up environment variables — create `backend/.env`:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://127.0.0.1:8000/callback
GROQ_API_KEY=your_groq_key
```

3. Run with Docker:
```bash
docker build -t music-personality .
docker run -p 8000:8000 --env-file backend/.env music-personality
```

4. Visit `http://127.0.0.1:8000`

## 📁 Project Structure
```
music-personality/
├── backend/
│   ├── main.py          # FastAPI routes
│   ├── spotify.py       # Spotify API integration
│   ├── ml_model.py      # K-Means clustering
│   ├── personality.py   # LLM personality generation
│   └── requirements.txt
├── frontend/
│   └── index.html       # Retro vinyl UI
├── Dockerfile
└── README.md
```

## 🌐 Live Demo

**[musiself.mooo.com](https://musiself.mooo.com)**

---

Built with ♪ by Aamina
