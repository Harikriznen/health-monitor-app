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

# Handle private key - replace escaped newlines with actual newlines
if private_key:
    private_key = private_key.replace('\\n', '\n')
    logger.info("Private key successfully loaded from environment")
else:
    # Fallback for development - this should NOT be used in production
    logger.warning("FIREBASE_PRIVATE_KEY not set - using fallback (development only)")
    private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDQKo85SMeO6YhN\nsytNebJF41IMObFQxzATN4+6sEh/Be/ddJ9Uay4xD3yMMHUblrNRsJaIBnzvLBcq\nPWUSHQr+qI+kz6OZ5lfOeMA8RG1mP4xgD/Jhkz+jWgeH0ZlvUpzn8OWQ/QRRbl9F\nQXaZBW815HDJpXh9gToaH9djXR2TlFIqmDbURjWhxOgim6RVmxx4SurJZdTF3nc8\n017LDsgqwyI1iPcAjTW23cWR8wHFQZiUshcTG+V09rZbcBz21sof709uRbpmhJqA\ncKZSX49ScIE1FG5GEJjLyWRQ/dzJd77MelD3uR9+xsj3+U2EwJn32Fc4arnzBqkd\nE5v0/fQvAgMBAAECggEAJfFT+MuIwEZV11/MiUsg0PdNybesV75ux1ntw0gFds20\numda8U619TBO8diVR+mQlte6oGGaXRfqwwK8zO/pRKChyhckyVUAdTxyQanxTN1R\nb2MIuXtW8qXi0IFGV9G1kttIZMSRiGw3Rk7X2K1yZ17TphWYoDuxRPi/0Dc1QGRI\n6q2LPP+J4vEP99WDbsqHk/AH0kpK5FiqwvXbY70A5u/4NE2msIIuZYd+KMliuFCG\n3CYrV/ORn8Jj8gtrU/gYYDe1vJcG0JCgIi+YjVj/F7l9cd2JkuJ/Syf/sGdujkSs\n8B/ysefhopYbd9CvdwscOlCyZJM3dRyy6q2lrp83KQKBgQDphpdmK/Ah+eYMXyxz\nw8ie+3oflxPhKE+SuwtTd+TQhvwqwzBaWSd190fCE2pgXmp1SMoPBO5Cj+QxexIl\nxxktwRlpHYDaHMtUjUWz0ybVzFRX1A/VksPKr3kfjVgj55sdWDsuIQdpwbVjduFq\nOjiyWblDXbU0D9xwQuywLTyJFwKBgQDkMy6q8wxeVNEtSbKl0ispkNcZedTxUcRy\nDcOUQ8dtF36tjEJIBVHy+U/Vu9tJ1OymiLyXd4BK8nHcFEZnwOGpF/OoOXUieYEy\nFnLMllrdcph6L7eTc5iJijbl5I0yFv6E07ZDJgSlTUqHjG1Ft58/ZjXdVvC2u0S1\nsvm0jvSsqQKBgQCzvtER54fx3vPfWfJROMVW+aHKZvL6P5jgC/Bv0rzgdMXr9Eln\ngXAKMMee7mrWulWe6OP+I4Fw4mh2XZBeW51ZxmPUsMzZFYi8D/EytLgToC7bW3LE\npS7m96F3U8gf+sk+EQecPfgCwwLnCD4BEcdKIB2laJ9s7zhxgFHGWUtbCQKBgQC1\nKHik13v7KwRAGqCLCVSgk85e+Bv3U31LOegIvOIFlcBID+/Scv7Cj+8z8wU8EJ+p\n+SUWbZTYaq2/FA1scm/yqAQTiUGXE7Rfyfhqt/X8lOu9HEJ0+TCgB6xbRtxcZmq5\nkcTAe972R2yiPPXGgeYXE5IxW8KOng4G3MVk9JQCuQKBgQCe53axVoVkRjRNGL80\nMfg/IQ0mAhe3uJbLukn/m+qd+VerasMr8cfZ9sEtOeGzfZrea0PLnboslU1eMk17\nZRR/9PQjeeNNUd2MmVv0SFZBC7yL5vpyvkBO319fQSJER+Kwj8KOX8iwRciTYswq\nUMEindW3I5thfQsXuAsUcRu7EQ==\n-----END PRIVATE KEY-----"

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
