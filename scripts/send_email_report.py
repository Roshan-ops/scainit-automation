import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")

REPORT_PATH = "reports/report.html"
SUMMARY_PATH = "reports/summary.txt"


def validate_env():
    required = {
        "SMTP_SERVER": SMTP_SERVER,
        "SMTP_USERNAME": SMTP_USERNAME,
        "SMTP_PASSWORD": SMTP_PASSWORD,
        "EMAIL_FROM": EMAIL_FROM,
        "EMAIL_TO": EMAIL_TO,
    }

    missing = [key for key, value in required.items() if not value]
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")


def send_email():
    validate_env()

    msg = EmailMessage()
    msg["Subject"] = "ScAinit Automation Test Report"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    summary_text = "No summary available."

    if os.path.exists(SUMMARY_PATH):
        with open(SUMMARY_PATH, "r", encoding="utf-8", errors="ignore") as file:
            summary_text = file.read()

    body = f"""
Hello,

The latest GitLab CI test execution for ScAinit automation has completed.

Test Summary:
{summary_text}

The HTML report is attached if available.

Regards,
ScAinit Automation Pipeline
"""
    msg.set_content(body)

    if os.path.exists(REPORT_PATH):
        with open(REPORT_PATH, "rb") as file:
            msg.add_attachment(
                file.read(),
                maintype="text",
                subtype="html",
                filename="report.html"
            )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)


if __name__ == "__main__":
    send_email()