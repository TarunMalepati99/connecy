# Conecy – Python Flask App

A full-stack Python implementation of the Conecy peer support platform.

## Features

- **Safe Space Agreement** – Community guidelines gate with checkbox agreement
- **Home Screen** – Choose to share or listen
- **Find a Listener** – Animated loading screen, auto-connects to chat
- **Live Chat** – Real-time chat UI with simulated listener responses + content moderation
- **Community Stories** – Browse, filter by category, and post anonymous stories
- **Listener Training** – 4 progressive training modules with progress tracking
- **Content Moderation** – Server-side filtering blocks offensive language

## Setup

### Requirements
- Python 3.8+

### Install and Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open: **http://localhost:5000**

## App Flow

```
/ (Landing)
└── /safe-space (Agreement)
    ├── /find-listener → /chat  (needs someone to listen)
    └── /training → /home       (wants to listen)
/community                       (browse & share stories)
```

## Architecture

- **Backend**: Flask (Python)
- **Frontend**: Jinja2 templates + vanilla JS + CSS custom properties
- **Storage**: In-memory (replace with PostgreSQL/SQLite for production)
- **Moderation**: Keyword-based server-side filtering

## Notes

- For production, replace in-memory storage with a real database
- WebSocket support (e.g. Flask-SocketIO) would enable real-time chat
- Add proper authentication for a production deployment
