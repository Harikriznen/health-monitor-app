import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from firebase_admin import credentials, firestore, initialize_app
from werkzeug.security import generate_password_hash, check_password_hash
import firebase_admin

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'devsecret')

from firebase_config import firebase_config
# Firebase setup
cred = credentials.Certificate(firebase_config)
if not firebase_admin._apps:
    default_app = initialize_app(cred)
db = firestore.client()

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
    metrics_ref = db.collection('metrics').document(current_user.id).get()
    metrics = metrics_ref.to_dict() if metrics_ref.exists else {}
    return render_template('dashboard.html', metrics=metrics)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
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
    if not request.is_json:
        return {'error': 'JSON required'}, 400
    data = request.get_json()
    metrics = data.get('metrics')
    if not metrics:
        return {'error': 'Missing metrics'}, 400
    db.collection('metrics').document(current_user.id).set(metrics)
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True)
