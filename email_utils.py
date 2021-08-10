import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(logger, desired_following, actual_following, lang):
    logger.info('sending email')

    subject, content = create_email_content(logger, desired_following, actual_following, lang)

    port = int(os.getenv('SMTP_PORT'))
    smtp_server = os.getenv('SMTP_SERVER')
    sender_email = os.getenv('SENDER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText(content, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    os.environ['IFC_EMAIL_SENT'] = '1'


def create_email_content(logger, desired_following, actual_following, lang):
    logger.info('creating email content')

    if lang == "ES":
        subject = "Revisa tu contador de followings en IG; algo huele a mierda en Dinamarca."
        content = f"Dices que quieres sequir {desired_following} cuentas, pero ahora mismo estás siguiendo {actual_following}. ¿Qué cojones?"
    else:
        subject = "Check your IG following count, something's wrong."
        content = f"You said you wanted to follow {desired_following} accounts, but you're currently following {actual_following}. The fuck?"

    logger.info(f'subject: {subject}')
    logger.info(f'content: {content}')

    return subject, content
