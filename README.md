# Email Notification Automation Script

This Python script automates the process of sending notifications for new, unseen emails from specific senders. It is designed to help users stay informed about important emails without being overwhelmed by every incoming message.


## Prerequisites

-  Python 3.x
- `imaplib2` and `smtplib` libraries (included in Python standard library)
- `python-dotenv` library for loading environment variables

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/lakshmivenkateshwaran/Email-Notification-Trigger.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Email_Automation
    ```
3. Install the required dependencies:
    ```bash
    pip install python-dotenv
    ```

## Setup

1. Create a `.env` file in the project directory with the following content:
    ```plaintext
    EMAIL_ACCOUNT=your-email@gmail.com
    PASSWORD=your-app-specific-password
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    NOTIFICATION_EMAIL=your-notification-email@example.com
    ```
   - Replace `your-email@gmail.com` with your Gmail address.
   - Replace `your-app-specific-password` with an app-specific password (not your regular email password).
   - Replace `your-notification-email@example.com` with the email address or phone number for receiving notifications.

2. Update the `email_addresses` list in the script with the email addresses you want to monitor:
    ```python
    email_addresses = [
        'important.sender1@example.com',
        'important.sender2@example.com',
        'important.sender3@example.com'
    ]
    ```

## Usage

Run the script using Python:
```bash
python main.py
