import aiosmtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from core.config import settings


async def send_email(
    recipient: str,
    subject: str,
    html_content: str,
    plain_content: str = "",
):
    message = MIMEMultipart("alternative")
    message["From"] = settings.superuser_info.email
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

    await aiosmtplib.send(
        message,
        hostname="127.0.0.1",
        port=1025,
    )
