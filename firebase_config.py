import os

# Firebase service account configuration
# Set these environment variables in production for security:
# FIREBASE_PROJECT_ID, FIREBASE_PRIVATE_KEY_ID, FIREBASE_PRIVATE_KEY, FIREBASE_CLIENT_EMAIL

firebase_config = {
	"type": "service_account",
	"project_id": os.environ.get("FIREBASE_PROJECT_ID", "newnod-4933c"),
	"private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID", "0ce141ea12d103a489d7c2825bcd471b88b00786"),
	"private_key": os.environ.get("FIREBASE_PRIVATE_KEY"),
	"client_email": os.environ.get("FIREBASE_CLIENT_EMAIL", "firebase-adminsdk-pxbd3@newnod-4933c.iam.gserviceaccount.com"),
	"client_id": "117473892018168923058",
	"auth_uri": "https://accounts.google.com/o/oauth2/auth",
	"token_uri": "https://oauth2.googleapis.com/token",
	"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
	"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-pxbd3%40newnod-4933c.iam.gserviceaccount.com",
	"universe_domain": "googleapis.com"
}
