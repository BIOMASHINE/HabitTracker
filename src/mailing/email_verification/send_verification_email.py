from core.models import User
from jinja_templates import templates
from mailing.send_email import send_email


async def send_verification_email(
    user: User,
    verification_link: str,
    verification_token: str,
):
    recipient = user.email
    subject = 'Confirm your email'
    template = templates.get_template('mailing/email-verify/verification-request.html')
    context = {
        'user': user,
        'verification_link': verification_link,
        'verification_token': verification_token,
    }
    html_content = template.render(context)

    await send_email(
        recipient=recipient,
        subject=subject,
        html_content=html_content,
        plain_content='',
    )
