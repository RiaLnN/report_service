from fastapi import APIRouter
from app.services.scraper import parse_page
from app.services.pdf_generator import generate_pdf

router = APIRouter()


@router.get('/report')
async def get_report(reps_count: int = 5):
    result = await parse_page(reps_count=reps_count)
    generate_pdf(result)
