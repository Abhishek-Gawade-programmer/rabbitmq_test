import pika
import json
import logging


def callback(ch, method, properties, body):
    message = json.loads(body)
    logging.info(f"Received: {message}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

    channel = connection.channel()
    channel.queue_declare(queue="test_queue")

    channel.basic_consume(
        queue="test_queue", on_message_callback=callback, auto_ack=True
    )

    logging.info("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Consumer started")
    main()
