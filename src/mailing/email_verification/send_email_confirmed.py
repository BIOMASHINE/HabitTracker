from core.models import User
from jinja_templates import templates
from mailing.send_email import send_email


async def send_email_confirmed(
    user: User,
):
    recipient = user.email
    subject = 'Email confirmed'
    template = templates.get_template('mailing/email-verify/email-verified.html')
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
