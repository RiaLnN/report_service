FROM python:3

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["celery", "-A", "tasks", "worker", "--loglevel=INFO"]
