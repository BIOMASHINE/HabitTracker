import aiosmtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import logging

from core.config import settings


logger = logging.getLogger(__name__)

async def send_email(
    recipient: str,
    subject: str,
    html_content: str,
    plain_content: str = "",
):
    message = MIMEMultipart("alternative")
    message["From"] = f'HabitTracker <{settings.smtp.smtp_user}>'
    message["To"] = recipient
    message["Subject"] = subject

    html_message = MIMEText(
        html_content,
        "html",
        "utf-8",
    )
    message.attach(html_message)

    if plain_content:
        plain_text_message = MIMEText(
            plain_content,
            "plain",
            "utf-8",
        )
        message.attach(plain_text_message)
        
    try:
        await aiosmtplib.send(
            message,
            hostname=settings.smtp.smtp_host,
            port=settings.smtp.smtp_port,
            username=settings.smtp.smtp_user,
            password=settings.smtp.smtp_password,
            use_tls=True,
        )
        logger.info(f"Email sent to {recipient}")
    except Exception as e:
        logger.error(f"Failed to send email to {recipient}: {e}", exc_info=True)
        raise
