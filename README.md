# report_service

## Stack
- Python 3
- FastAPI
- Celery + Celery Beat
- Redis
- Jinja2 + WeasyPrint
- BeautifulSoup4 + httpx
- Docker Compose

## Run

### Docker Compose (recommended)
1. Create a `.env` file in the project root:
   - `MAIL=your_email@gmail.com`
   - `MAIL_PASSWORD=your_app_password`
2. Start services:
   ```bash
   docker compose up --build
   ```
3. This starts:
   - `app` — Celery worker (report generation and sending)
   - `celery-beat` — scheduler
   - `redis` — task broker

### Local (API)
1. Install dependencies:
   ```bash
   cd app
   pip install -r requirements.txt
   ```
2. Run API:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
3. Generate a report:
   ```bash
   curl "http://localhost:8000/report?reps_count=5"
   ```

## Customization
- Number of repositories in API response: `reps_count` (`/report?reps_count=N`).
- Default count for scheduled task: `reps_count=5` in `app/tasks.py`.
- Weekly schedule time: `crontab(day_of_week='sunday', hour=23, minute=0)` in `app/core/celery.py`.
- Trending source URL: `GIT_HUB_TRENDING_URL` in `app/core/constants.py`.
- Mail settings: `MAIL` and `MAIL_PASSWORD` (loaded from `.env` in `app/core/config.py`).
