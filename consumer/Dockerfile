FROM python:3.8-slim
WORKDIR /app
COPY consumer.py .
RUN pip install pika
CMD ["sh", "-c", "sleep 5 && python consumer.py"]
