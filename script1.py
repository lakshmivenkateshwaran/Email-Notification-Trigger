# This code contains single email notification script.

import os
from dotenv import load_dotenv
import imaplib
import email
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

# Email configuration

IMAP_SERVER = 'imap.gmail.com'  # Gmail's IMAP server
EMAIL_ACCOUNT = os.getenv('EMAIL_ACCOUNT')
PASSWORD = os.getenv('PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL')

# Function to send notification
def send_notification(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ACCOUNT
    msg['To'] = NOTIFICATION_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ACCOUNT, PASSWORD)
        server.sendmail(EMAIL_ACCOUNT, NOTIFICATION_EMAIL, msg.as_string())

try:
    # Connect to the email server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.select('inbox')

    # Fetch unseen emails from "bharathivasudevan538@gmail.com"
    result, data = mail.search(None, '(UNSEEN FROM "bharathivasudevan538@gmail.com")')
    email_ids = data[0].split()

    # Process unseen emails
    if email_ids:
        for email_id in email_ids:
            result, message_data = mail.fetch(email_id, '(RFC822)')
            raw_email = message_data[0][1]
            msg = email.message_from_bytes(raw_email)
            sender = msg['from']
            subject = msg['subject']

            # Send notification for each unseen email
            notification_subject = 'New Email from bharathivasudevan538@gmail.com'
            notification_body = f'From: {sender}\nSubject: {subject}'
            send_notification(notification_subject, notification_body)

    print(f'Sent notifications for {len(email_ids)} new emails from bharathivasudevan538@gmail.com.')

except imaplib.IMAP4.error as e:
    print(f'IMAP error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
finally:
    # Close the connection
    try:
        mail.close()
        mail.logout()
    except:
        pass  # Handle logout errors gracefully
