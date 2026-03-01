# Health Monitor WebApp

A Flask-based web application for real-time health monitoring dashboards, user authentication, and Firebase integration. Users can log in, view health metrics, and data is synced to Firebase for online access.

## Features
- User authentication (login/register)
- Dashboard with health metrics (BP, SpO2, Pulse, Resp Rate, Arrhythmia, etc.)
- Real-time sync with Firebase (Firestore or Realtime DB)
- Responsive UI with Bootstrap

## Setup
1. Create a Python virtual environment and activate it.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Firebase credentials (see below).
4. Run the app: `python app.py`

## Firebase Setup
- Create a Firebase project at https://console.firebase.google.com/
- Download your service account key JSON and place it as `firebase_key.json` in the project root.
- Update `firebase_config.py` with your Firebase project details.

## Folder Structure
- `app.py` - Main Flask app
- `firebase_config.py` - Firebase setup
- `templates/` - HTML templates
- `static/` - CSS/JS assets

---
*Replace this README with more details as you build your app.*
