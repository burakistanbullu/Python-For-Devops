import os
import smtplib
import logging
from email.mime.text import MIMEText
from pathlib import Path
import subprocess

# Basic logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# Configuration from environment variables
TERRAFORM_DIR = Path(os.getenv("TERRAFORM_DIR", ""))
EMAIL_FROM = os.getenv("EMAIL_FROM", "")
EMAIL_TO = os.getenv("EMAIL_TO", "")
SMTP_SERVER = os.getenv("SMTP_SERVER", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# Function to send email
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string())
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")

# Function to run terraform plan
def run_terraform_plan():
    result = subprocess.run(['terraform', 'plan', '-detailed-exitcode','-no-color'], cwd=TERRAFORM_DIR, capture_output=True, text=True, timeout=300)
    return result.returncode, result.stdout + result.stderr

# Main function to check infrastructure
def check_infrastructure():
    returncode, output = run_terraform_plan()
    if returncode == 2:  # Changes present
        logging.info('Terraform Plan Detected Changes', f'The following changes were detected:\n\n{output}')
        send_email('Terraform Plan Detected Changes', f'The following changes were detected:\n\n{output}')
    elif returncode == 0:
        logging.info("No changes detected.")
    else:
        logging.error(f"Error running terraform plan:\n{output}")

#  Execute the main function
if __name__ == "__main__":
    check_infrastructure()