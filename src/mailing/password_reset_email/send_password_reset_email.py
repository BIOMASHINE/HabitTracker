from core.models import User
from jinja_templates import templates
from mailing.send_email import send_email


async def send_password_reset_email(
    user: User,
    password_reset_link: str,
    password_reset_token: str,
):
    recipient = user.email
    subject = 'Reset your password'
    template = templates.get_template('mailing/password-reset-email/reset-password-email.html')
    context = {
        'user': user,
        'password_reset_link': password_reset_link,
        'password_reset_token': password_reset_token,
    }
    html_content = template.render(context)

    await send_email(
        recipient=recipient,
        subject=subject,
        html_content=html_content,
        plain_content='',
    )
