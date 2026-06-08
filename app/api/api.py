from fastapi import APIRouter
from app.api import report

router = APIRouter()

router.include_router(report.router)