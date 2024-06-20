# Dockerfile
FROM python:3.10

WORKDIR /app

COPY user_service.py /app

RUN pip install flask

CMD ["python", "user_service.py"]
