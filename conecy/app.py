from flask import Flask, render_template, request, jsonify, session
import uuid
import random
import re
import time

app = Flask(__name__)
app.secret_key = 'conecy-secret-key-2024'

# In-memory storage (replace with DB in production)
community_stories = []
listeners_queue = []
active_chats = {}

OFFENSIVE_WORDS = ['hate', 'kill', 'stupid', 'idiot', 'dumb', 'loser']

def moderate_message(text):
    text_lower = text.lower()
    for word in OFFENSIVE_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
            return False, f"Message blocked: contains inappropriate language ('{word}'). Please keep this a safe space."
    return True, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/safe-space')
def safe_space():
    return render_template('safe_space.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/find-listener')
def find_listener():
    return render_template('find_listener.html')

@app.route('/chat')
def chat():
    listener_id = random.randint(100, 999)
    session['listener_id'] = listener_id
    return render_template('chat.html', listener_id=listener_id)

# API Routes
@app.route('/api/stories', methods=['GET'])
def get_stories():
    category = request.args.get('category', 'all')
    if category == 'all':
        return jsonify(community_stories)
    return jsonify([s for s in community_stories if s['category'] == category])

@app.route('/api/stories', methods=['POST'])
def post_story():
    data = request.json
    text = data.get('content', '')
    ok, err = moderate_message(text)
    if not ok:
        return jsonify({'error': err}), 400
    story = {
        'id': str(uuid.uuid4()),
        'content': text,
        'category': data.get('category', 'Other'),
        'timestamp': time.strftime('%B %d, %Y'),
        'responses': random.randint(0, 12)
    }
    community_stories.append(story)
    return jsonify(story), 201

@app.route('/api/chat/send', methods=['POST'])
def send_chat():
    data = request.json
    text = data.get('message', '')
    ok, err = moderate_message(text)
    if not ok:
        return jsonify({'error': err, 'blocked': True}), 400
    return jsonify({'status': 'sent', 'message': text})

@app.route('/api/moderate', methods=['POST'])
def check_moderation():
    data = request.json
    text = data.get('text', '')
    ok, err = moderate_message(text)
    return jsonify({'ok': ok, 'error': err})

if __name__ == '__main__':
    # Add some sample stories
    community_stories.extend([
        {
            'id': '1',
            'content': 'Moving to a new city for my first job was terrifying. I knew nobody. For weeks I ate lunch alone. But slowly I found my people — through a hiking group I almost didn\'t join. It gets better.',
            'category': 'New City',
            'timestamp': 'February 28, 2026',
            'responses': 8
        },
        {
            'id': '2',
            'content': 'First semester nearly broke me. I went from top of my class in high school to feeling completely lost. Turns out everyone else felt the same way. We just weren\'t talking about it.',
            'category': 'First Semester',
            'timestamp': 'March 1, 2026',
            'responses': 14
        },
        {
            'id': '3',
            'content': 'As an F1 student, the visa stress alone is overwhelming. Add classes, language barriers, and being 8,000 miles from family — it\'s a lot. Finding this community helped more than I can say.',
            'category': 'F1 Student',
            'timestamp': 'March 3, 2026',
            'responses': 11
        }
    ])
    app.run(debug=True, port=5000)
