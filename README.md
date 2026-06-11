# report_service

## Стек
- Python 3
- FastAPI
- Celery + Celery Beat
- Redis
- Jinja2 + WeasyPrint
- BeautifulSoup4 + httpx
- Docker Compose

## Запуск

### Через Docker Compose (рекомендуется)
1. Создайте файл `.env` в корне проекта:
   - `MAIL=your_email@gmail.com`
   - `MAIL_PASSWORD=your_app_password`
2. Запустите сервисы:
   ```bash
   docker compose up --build
   ```
3. Что поднимется:
   - `app` — Celery worker (генерация и отправка отчётов)
   - `celery-beat` — планировщик задач
   - `redis` — брокер задач

### Локально (API)
1. Установите зависимости:
   ```bash
   cd app
   pip install -r requirements.txt
   ```
2. Запустите API:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
3. Сформируйте отчёт:
   ```bash
   curl "http://localhost:8000/report?reps_count=5"
   ```

## Кастомизация
- Количество репозиториев в API-запросе: параметр `reps_count` (`/report?reps_count=N`).
- Значение по умолчанию для периодической задачи: `reps_count=5` в `app/tasks.py`.
- Время еженедельного запуска: `crontab(day_of_week='sunday', hour=23, minute=0)` в `app/core/celery.py`.
- URL источника трендов: `GIT_HUB_TRENDING_URL` в `app/core/constants.py`.
- Настройки почты: `MAIL` и `MAIL_PASSWORD` (читаются из `.env` в `app/core/config.py`).
