FROM python:3.9-slim

WORKDIR /app

# 시스템 패키지
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# requirements 먼저 복사 (캐시 최적화)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 앱 복사
COPY app ./app

# 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
