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

# Fallback private key if environment variable is not set
# This is used for both local development and as fallback
fallback_private_key = """-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDQKo85SMeO6YhN
sytNebJF41IMObFQxzATN4+6sEh/Be/ddJ9Uay4xD3yMMHUblrNRsJaIBnzvLBcq
PWUSHQr+qI+kz6OZ5lfOeMA8RG1mP4xgD/Jhkz+jWgeH0ZlvUpzn8OWQ/QRRbl9F
QXaZBW815HDJpXh9gToaH9djXR2TlFIqmDbURjWhxOgim6RVmxx4SurJZdTF3nc8
017LDsgqwyI1iPcAjTW23cWR8wHFQZiUshcTG+V09rZbcBz21sof709uRbpmhJqA
cKZSX49ScIE1FG5GEJjLyWRQ/dzJd77MelD3uR9+xsj3+U2EwJn32Fc4arnzBqkd
E5v0/fQvAgMBAAECggEAJfFT+MuIwEZV11/MiUsg0PdNybesV75ux1ntw0gFds20
umda8U619TBO8diVR+mQlte6oGGaXRfqwwK8zO/pRKChyhckyVUAdTxyQanxTN1R
b2MIuXtW8qXi0IFGV9G1kttIZMSRiGw3Rk7X2K1yZ17TphWYoDuxRPi/0Dc1QGRI
6q2LPP+J4vEP99WDbsqHk/AH0kpK5FiqwvXbY70A5u/4NE2msIIuZYd+KMliuFCG
3CYrV/ORn8Jj8gtrU/gYYDe1vJcG0JCgIi+YjVj/F7l9cd2JkuJ/Syf/sGdujkSs
8B/ysefhopYbd9CvdwscOlCyZJM3dRyy6q2lrp83KQKBgQDphpdmK/Ah+eYMXyxz
w8ie+3oflxPhKE+SuwtTd+TQhvwqwzBaWSd190fCE2pgXmp1SMoPBO5Cj+QxexIl
xxktwRlpHYDaHMtUjUWz0ybVzFRX1A/VksPKr3kfjVgj55sdWDsuIQdpwbVjduFq
OjiyWblDXbU0D9xwQuywLTyJFwKBgQDkMy6q8wxeVNEtSbKl0ispkNcZedTxUcRy
DcOUQ8dtF36tjEJIBVHy+U/Vu9tJ1OymiLyXd4BK8nHcFEZnwOGpF/OoOXUieYEy
FnLMllrdcph6L7eTc5iJijbl5I0yFv6E07ZDJgSlTUqHjG1Ft58/ZjXdVvC2u0S1
svm0jvSsqQKBgQCzvtER54fx3vPfWfJROMVW+aHKZvL6P5jgC/Bv0rzgdMXr9Eln
gXAKMMee7mrWulWe6OP+I4Fw4mh2XZBeW51ZxmPUsMzZFYi8D/EytLgToC7bW3LE
pS7m96F3U8gf+sk+EQecPfgCwwLnCD4BEcdKIB2laJ9s7zhxgFHGWUtbCQKBgQC1
KHik13v7KwRAGqCLCVSgk85e+Bv3U31LOegIvOIFlcBID+/Scv7Cj+8z8wU8EJ+p
+SUWbZTYaq2/FA1scm/yqAQTiUGXE7Rfyfhqt/X8lOu9HEJ0+TCgB6xbRtxcZmq5
kcTAe972R2yiPPXGgeYXE5IxW8KOng4G3MVk9JQCuQKBgQCe53axVoVkRjRNGL80
Mfg/IQ0mAhe3uJbLukn/m+qd+VerasMr8cfZ9sEtOeGzfZrea0PLnboslU1eMk17
ZRR/9PQjeeNNUd2MmVv0SFZBC7yL5vpyvkBO319fQSJER+Kwj8KOX8iwRciTYswq
UMEindW3I5thfQsXuAsUcRu7EQ==
-----END PRIVATE KEY-----"""

# Use environment variable if set, otherwise use fallback
if private_key:
    # Handle private key - convert escaped newlines to actual newlines
    private_key = private_key.replace('\\n', '\n')
    logger.info("Private key loaded from environment variable")
else:
    # Use fallback private key
    private_key = fallback_private_key
    logger.info("Using fallback private key")

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
