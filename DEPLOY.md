# Deployment Instructions

## Option 1: Deploy to Render.com (Recommended - Free)

1. **Push code to GitHub:**
   - Go to https://github.com/new
   - Create a new repository named "health-monitor-app"
   - Run these commands in your terminal:
     
```
     gh auth login
     gh repo create health-monitor-app --public --source=. --description "Health Monitor Flask app with Firebase"
     git push -u origin master
     
```

2. **Deploy on Render:**
   - Go to https://dashboard.render.com/
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Select your "health-monitor-app" repository
   - Configure:
     - Name: health-monitor
     - Environment: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
   - Add these Environment Variables:
     - `SECRET_KEY`: Generate a secure random key
   - Click "Create Web Service"

## Option 2: Deploy to PythonAnywhere (Easier)

1. Sign up at https://www.pythonanywhere.com/
2. Go to the "Web" tab
3. Click "Add a new web app"
4. Select "Flask" and Python version
5. Upload your files via the "Files" tab
6. Set up your Firebase credentials as environment variables

## Option 3: Deploy to Heroku

1. Install Heroku CLI
2. Run:
   
```
   heroku login
   heroku create health-monitor-app
   git push heroku master
   
```

## Firebase Configuration for Production

In `firebase_config.py`, replace the hardcoded credentials with environment variables:
```
python
import os

firebase_config = {
    "type": "service_account",
    "project_id": os.environ.get('FIREBASE_PROJECT_ID'),
    "private_key_id": os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
    "private_key": os.environ.get('FIREBASE_PRIVATE_KEY'),
    "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{os.environ.get('FIREBASE_CLIENT_EMAIL')}%40{os.environ.get('FIREBASE_PROJECT_ID')}.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
