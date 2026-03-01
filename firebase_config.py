import os
import logging

# Firebase service account configuration
# Set these environment variables in production for security:
# FIREBASE_PROJECT_ID, FIREBASE_PRIVATE_KEY_ID, FIREBASE_PRIVATE_KEY, FIREBASE_CLIENT_EMAIL

# Debug: Print all environment variables (excluding sensitive values)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Checking Firebase environment variables...")
logger.info(f"FIREBASE_PROJECT_ID: {os.environ.get('FIREBASE_PROJECT_ID', 'NOT SET')}")
logger.info(f"FIREBASE_PRIVATE_KEY_ID: {os.environ.get('FIREBASE_PRIVATE_KEY_ID', 'NOT SET')}")
logger.info(f"FIREBASE_PRIVATE_KEY present: {bool(os.environ.get('FIREBASE_PRIVATE_KEY'))}")
logger.info(f"FIREBASE_CLIENT_EMAIL: {os.environ.get('FIREBASE_CLIENT_EMAIL', 'NOT SET')}")

# Get environment variables, with fallback defaults for development
project_id = os.environ.get("FIREBASE_PROJECT_ID", "newnod-4933c")
private_key_id = os.environ.get("FIREBASE_PRIVATE_KEY_ID", "c41810fca24f71ca01b4a819760e0c4ab3591285")
private_key = os.environ.get("FIREBASE_PRIVATE_KEY")
client_email = os.environ.get("FIREBASE_CLIENT_EMAIL", "firebase-adminsdk-pxbd3@newnod-4933c.iam.gserviceaccount.com")

# Handle private key - convert escaped newlines to actual newlines
# Handle multiple cases: \\n, \n, or actual newlines
if private_key:
    # First replace escaped backslash-n with actual newlines
    private_key = private_key.replace('\\n', '\n')
    # Then replace any remaining literal \n with actual newlines
    private_key = private_key.replace('\n', '\n')
    logger.info("Private key successfully loaded from environment")

firebase_config = {
	"type": "service_account",
	"project_id": project_id,
	"private_key_id": private_key_id,
	"private_key": private_key,
	"client_email": client_email,
	"client_id": "117473892018168923058",
	"auth_uri": "https://accounts.google.com/o/oauth2/auth",
	"token_uri": "https://oauth2.googleapis.com/token",
	"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
	"client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{client_email.replace('@', '%40').replace('.', '%2E')}@%40{project_id}.iam.gserviceaccount.com",
	"universe_domain": "googleapis.com"
}
