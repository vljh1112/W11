# 베이스 이미지
FROM python:3.10-slim

# 작업 디렉토리
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

# Flask 실행 (0.0.0.0:5000)
CMD ["python", "app/app.py"]