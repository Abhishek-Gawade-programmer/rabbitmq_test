import pika
import uuid
import time
import json
from datetime import datetime
import socket
import logging


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

    channel = connection.channel()
    channel.queue_declare(queue="test_queue")

    while True:
        message = {
            "message_id": str(uuid.uuid4()),
            "created_on": datetime.now().isoformat(),
        }
        channel.basic_publish(
            exchange="", routing_key="test_queue", body=json.dumps(message)
        )
        print(f"Sent: {message}")
        logging.info(f"Sent: {message}")
        time.sleep(5)


if __name__ == "__main__":
    print("Producer started")
    logging.basicConfig(level=logging.INFO)
    logging.info("Producer started")
    main()
