FROM python:3.12-slim

WORKDIR /app

COPY requirement.txt .

RUN python -m pip install --no-cache-dir -r requirement.txt

COPY app.py .
COPY query_db.py .
COPY test_app.py .

CMD ["python", "app.py"]