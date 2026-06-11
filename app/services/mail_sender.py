import smtplib
from email.message import EmailMessage
from core.constants import SUBJECT, MAIL_CONTENT
from core.config import settings

def send_email(pdf_path, recipient_email):
    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = settings.MAIL
    msg['To'] = recipient_email
    msg.set_content(MAIL_CONTENT)

    with open(pdf_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='report.pdf')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(settings.MAIL, settings.MAIL_PASSWORD)
        smtp.send_message(msg)
