[README (2).md](https://github.com/user-attachments/files/25785685/README.2.md)
<div align="center">

<br/>

```
   ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗██╗   ██╗
  ██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔════╝╚██╗ ██╔╝
  ██║     ██║   ██║██╔██╗ ██║█████╗  ██║      ╚████╔╝ 
  ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║       ╚██╔╝  
  ╚██████╗╚██████╔╝██║ ╚████║███████╗╚██████╗   ██║   
   ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝  
```

### *Human connection, anonymously.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-6B5CF6?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-F5A623?style=flat-square)](CONTRIBUTING.md)
[![Status](https://img.shields.io/badge/Status-Active-22C55E?style=flat-square)]()

<br/>

> A safe space to be heard, or to offer your presence.  
> No judgments. No identity. Just genuine human support.

<br/>

---

</div>

<br/>

## ✦ What is Conecy?

Conecy is an **anonymous peer support platform** designed for people navigating life transitions — first semesters, new cities, first jobs, or simply hard days. It connects people who need to be heard with trained volunteer listeners, all without revealing anyone's identity.

Built for university communities and beyond, Conecy creates a psychologically safe environment where vulnerability is welcomed and no one faces their challenges alone.

```
Someone having a hard day  ──────────────────────────►  Someone who wants to help
        │                                                         │
        ▼                                                         ▼
  "I need someone                                        "I want to listen"
    to listen"                                                    │
        │                                                         ▼
        │                                              ┌─── Listener Training ───┐
        │                                              │  • Empathetic Listening  │
        │                                              │  • Active Techniques     │
        │                                              │  • Healthy Boundaries    │
        │                                              └─────────────────────────┘
        │                                                         │
        └──────────────────── Anonymous Chat ◄───────────────────┘
```

<br/>

---

## ✦ Features

<br/>

**🛡️ Safe Space Agreement**
A values-first onboarding that sets clear community expectations before anyone enters. Every user agrees to uphold the guidelines — no harassment, no diagnosing, no judgment.

**🤍 Need Someone / Want to Listen**
Two clear paths. People seeking support are matched with trained listeners. People who want to help complete a short training program before going live.

**💬 Anonymous Chat**
Real-time chat with fully anonymized identities. Listeners are identified only by a number. Content moderation runs on every message server-side.

**📖 Community Stories**
An open board where users share experiences from their transitions — filterable by category. Stories of perseverance, loneliness, growth, and hope, written by real people.

**🎓 Listener Training**
Four progressive modules that unlock sequentially, teaching empathetic listening, active techniques, appropriate language, and healthy boundaries.

**🔍 Content Moderation**
Every message — whether a community post or a chat message — passes through server-side moderation before it's accepted. No "send anyway" option. Bad content is simply blocked.

<br/>

---

## ✦ App Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│   /  (Landing)                                                    │
│    │                                                              │
│    └──► /safe-space (Agreement)                                   │
│              │                                                    │
│              ├──► /find-listener ──► /chat   ← I need support    │
│              │         (orb loading)                              │
│              │                                                    │
│              └──► /training ──► /home        ← I want to listen  │
│                   (4 modules)                                     │
│                                                                   │
│   /community  (browse & share stories — always accessible)       │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

<br/>

---

## ✦ Screenshots

<br/>

| Safe Space Agreement | Home — Choose Your Path |
|:---:|:---:|
| *Community guidelines gate with checkbox* | *Two clear modes: share or listen* |
<img width="777" height="890" alt="Screenshot 2026-03-05 232147" src="https://github.com/user-attachments/assets/2fd2d8f9-b86f-4b5e-908f-cd3ad6215712" />
| Listener Training | Anonymous Chat |
|:---:|:---:|
| *4 progressive modules with progress tracking* | *Certified listener, fully anonymous* |
<img width="983" height="880" alt="Screenshot 2026-03-05 232208" src="https://github.com/user-attachments/assets/a57235ba-84e4-4d9a-8d6b-796d290450e8" />
| Community Stories | Finding a Listener |
|:---:|:---:|
| *Filter by life transition category* | *Breathing orb animation while matching* |
<img width="969" height="745" alt="Screenshot 2026-03-05 232222" src="https://github.com/user-attachments/assets/7d817527-ec23-4b7b-aba0-231d7f9a195f" />

<img width="1650" height="901" alt="Screenshot 2026-03-05 232138" src="https://github.com/user-attachments/assets/cb244337-131b-47b9-86d1-8030cd5dc056" />

<br/>

---

## ✦ Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/conecy.git
cd conecy

# 2. (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open your browser and navigate to:

```
http://localhost:5000
```

That's it. No database setup, no environment variables, no config files. It just runs.

<br/>

---

## ✦ Project Structure

```
conecy/
│
├── app.py                  # Flask application & API routes
├── requirements.txt        # Python dependencies
├── README.md               # You are here
│
└── templates/
    ├── base.html           # Shared layout, CSS design system, typography
    ├── index.html          # Landing page
    ├── safe_space.html     # Community agreement gate
    ├── home.html           # Dashboard (post-agreement)
    ├── find_listener.html  # Animated matching screen
    ├── chat.html           # Anonymous chat interface
    ├── community.html      # Story board with category filters
    └── training.html       # Listener training modules
```

<br/>

---

## ✦ API Reference

The Flask backend exposes a small REST API consumed by the frontend templates.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/stories` | Fetch all community stories (filterable with `?category=`) |
| `POST` | `/api/stories` | Submit a new anonymous story |
| `POST` | `/api/chat/send` | Send a chat message (runs moderation) |
| `POST` | `/api/moderate` | Check a text string against moderation rules |

**Example — Post a story:**
```bash
curl -X POST http://localhost:5000/api/stories \
  -H "Content-Type: application/json" \
  -d '{"content": "First semester was hard but I made it.", "category": "First Semester"}'
```

**Example — Moderation check:**
```bash
curl -X POST http://localhost:5000/api/moderate \
  -H "Content-Type: application/json" \
  -d '{"text": "This is a kind message"}'

# Response: {"ok": true, "error": null}
```

<br/>

---

## ✦ Content Moderation

Every user-submitted message passes through a server-side moderation pipeline before being stored or sent.

```python
# The moderation check — no "send anyway" escape hatch
def moderate_message(text):
    text_lower = text.lower()
    for word in OFFENSIVE_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
            return False, f"Message blocked: contains inappropriate language."
    return True, None
```

**Design principle:** Conecy does not show a "send anyway" option for flagged content. Blocked messages are simply blocked. This aligns with the platform's commitment to zero-tolerance for harmful communication.

For production deployments, this can be extended with:
- Machine learning classification (e.g. Perspective API)
- Regex pattern matching for more complex cases  
- Escalation queue for human moderator review

<br/>

---

## ✦ Tech Stack

| Layer | Technology |
|-------|-----------|
| Web Framework | [Flask](https://flask.palletsprojects.com/) |
| Templating | Jinja2 |
| Frontend | Vanilla JS + CSS custom properties |
| Typography | DM Sans + DM Serif Display (Google Fonts) |
| Storage | In-memory (Python lists/dicts) |
| Moderation | Keyword matching (regex) |

<br/>

---

## ✦ Roadmap

The current version is a functional prototype. Here's where it can go:

- [ ] **Real-time chat** via WebSockets (Flask-SocketIO)
- [ ] **Persistent storage** — PostgreSQL or SQLite backend
- [ ] **User authentication** — anonymous session tokens
- [ ] **ML moderation** — integrate Perspective API or similar
- [ ] **Listener queue** — real listener-to-user matching system
- [ ] **Mobile app** — React Native wrapper
- [ ] **Admin dashboard** — moderation review panel
- [ ] **Analytics layer** — aggregated trend insights for institutions
- [ ] **HIPAA compliance** — for university health-adjacent deployments
- [ ] **IRB-compatible data structure** — for research use at Indiana University

<br/>

---

## ✦ Architecture (Production Vision)

```
┌─────────────┐     HTTPS      ┌──────────────────────────────────┐
│  Client App │ ◄────────────► │         API Gateway              │
│  (Web/Mobile│                └──────────────┬───────────────────┘
└─────────────┘                               │
                                    ┌─────────▼─────────┐
                                    │   Flask Backend    │
                                    │                    │
                                    │  ┌─────────────┐   │
                                    │  │  User Svc   │   │
                                    │  ├─────────────┤   │
                                    │  │  Chat Svc   │   │
                                    │  ├─────────────┤   │
                                    │  │  Story Svc  │   │
                                    │  ├─────────────┤   │
                                    │  │  Mod Engine │   │
                                    │  └─────────────┘   │
                                    └─────────┬──────────┘
                                              │
                               ┌──────────────▼─────────────┐
                               │       PostgreSQL DB          │
                               │  users · stories · sessions │
                               └────────────────────────────┘
```

<br/>

---

## ✦ Privacy & Safety Principles

Conecy was designed privacy-first from the ground up:

- **No real names** — users are anonymous by default; listeners are identified only by number
- **Minimal PII** — the system collects the least data necessary to function
- **Encrypted communication** — all traffic over HTTPS in production
- **No "send anyway"** — harmful messages are blocked entirely, not warned about
- **Peer support disclaimer** — every community page reminds users this is not professional mental health care
- **Crisis line prompt** — the platform surfaces crisis resources when needed

> *For university deployments that interface with health services, HIPAA compliance considerations apply. Institutional research use may require IRB approval (e.g. Indiana University IRB).*

<br/>

---

## ✦ Contributing

Contributions are warmly welcomed. This is a product built around human kindness — the development process should reflect that too.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "Add: brief description of your change"
git push origin feature/your-feature-name
# Open a pull request
```

Please keep PRs focused and include a short description of what you changed and why. For larger features, open an issue first to discuss.

<br/>

---

<div align="center">

<br/>

*"Sometimes the most healing thing we can do*  
*is simply show up for someone."*

<br/>

**Built with care. Designed for connection.**

<br/>

---

[Report a Bug](../../issues) · [Request a Feature](../../issues) · [Start a Discussion](../../discussions)

<br/>

</div>
