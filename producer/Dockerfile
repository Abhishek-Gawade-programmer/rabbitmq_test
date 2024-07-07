FROM python:3.10-slim
WORKDIR /app
COPY producer.py .
RUN pip install pika
# sleep 10 seconds to wait for RabbitMQ to start
CMD ["sh", "-c", "sleep 5 && python producer.py"]
