FROM python:3.12

WORKDIR /app

COPY chat_service.py /app

RUN pip install websockets requests

CMD ["python", "chat_service.py"]
