from core.models import User
from jinja_templates import templates
from mailing.send_email import send_email


async def send_password_success_reset_email(
    user: User,
):
    recipient = user.email
    subject = 'Password was successfully changed'
    template = templates.get_template('mailing/password-reset-email/success-password-email.html')
    context = {
        'user': user,
    }
    html_content = template.render(context)

    await send_email(
        recipient=recipient,
        subject=subject,
        html_content=html_content,
        plain_content='',
    )
