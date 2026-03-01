import os
import logging
from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from firebase_admin import credentials, firestore, initialize_app
from werkzeug.security import generate_password_hash, check_password_hash
import firebase_admin

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'devsecret')

# Get port from environment (Render provides this)
port = int(os.environ.get('PORT', 5000))

# Initialize Firebase lazily
db = None

def init_firebase():
    global db
    if db is None:
        try:
            from firebase_config import firebase_config
            # Check if Firebase is already initialized
            if not firebase_admin._apps:
                cred = credentials.Certificate(firebase_config)
                default_app = initialize_app(cred)
                logger.info("Firebase initialized successfully")
            db = firestore.client()
        except Exception as e:
            logger.error(f"Firebase initialization error: {e}")
            raise

# Do NOT initialize Firebase at startup - it will be initialized on first request
# This allows the app to start even if Firebase config is missing

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, email, password_hash):
        self.id = id
        self.email = email
        self.password_hash = password_hash

    @staticmethod
    def get(user_id):
        if db is None:
            init_firebase()
        user_ref = db.collection('users').document(user_id).get()
        if user_ref.exists:
            data = user_ref.to_dict()
            return User(user_id, data['email'], data['password_hash'])
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
@login_required
def dashboard():
    if db is None:
        init_firebase()
    metrics_ref = db.collection('metrics').document(current_user.id).get()
    metrics = metrics_ref.to_dict() if metrics_ref.exists else {}
    return render_template('dashboard.html', metrics=metrics)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if db is None:
            init_firebase()
        email = request.form['email']
        password = request.form['password']
        users = db.collection('users').where(filter=('email', '==', email)).get()
        for user in users:
            data = user.to_dict()
            if check_password_hash(data['password_hash'], password):
                user_obj = User(user.id, data['email'], data['password_hash'])
                login_user(user_obj)
                return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if db is None:
            init_firebase()
        email = request.form['email']
        password = request.form['password']
        users = db.collection('users').where(filter=('email', '==', email)).get()
        if any(users):
            flash('Email already registered')
        else:
            user_ref = db.collection('users').document()
            user_ref.set({
                'email': email,
                'password_hash': generate_password_hash(password)
            })
            flash('Registration successful. Please log in.')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/api/metrics', methods=['POST'])
@login_required
def api_metrics():
    if db is None:
        init_firebase()
    if not request.is_json:
        return {'error': 'JSON required'}, 400
    data = request.get_json()
    metrics = data.get('metrics')
    if not metrics:
        return {'error': 'Missing metrics'}, 400
    db.collection('metrics').document(current_user.id).set(metrics)
    return {'status': 'success'}

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
