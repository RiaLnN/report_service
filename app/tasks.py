from core.celery import app
from services.scraper import parse_page
from services.pdf_generator import generate_pdf
from services.mail_sender import send_email
from core.config import settings
import asyncio

@app.task
def generate_github_report_task():
    data = asyncio.run(parse_page(reps_count=5))

    filename = "weekly_report.pdf"
    generate_pdf(data, filename)
    send_email(filename, settings.MAIL)

    return f"Report {filename} ready!"