## structure:

```
rabbitmq_test/
├── docker-compose.yml
├── producer/
│   ├── Dockerfile
│   ├── producer.py
├── consumer/
│   ├── Dockerfile
│   ├── consumer.py
└── README.md
```

## Setup and Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd rabbitmq_test
   ```

````

2. Start the services:

   ```bash
   docker-compose up
   ```

3. The producer will send a message to RabbitMQ every 5 seconds, and the consumer will log the received messages.

````

### 9. Run the Project

Navigate to the project directory and run:

```bash
docker-compose up
```

This will start the RabbitMQ server, the producer, and the consumer. The producer will send a message every 5 seconds, and the consumer will log the messages as they are received.
