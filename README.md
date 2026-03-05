# Learning Kafka with Python

A hands-on project to learn **Apache Kafka** fundamentals using Python and `confluent-kafka`.

## What This Project Covers

- Setting up Kafka locally using Docker (KRaft mode — no ZooKeeper)
- Producing messages to a Kafka topic
- Consuming messages from a Kafka topic
- Understanding offsets, partitions, and consumer groups

## Project Structure

```
kafka/
├── docker-compose.yaml   # Kafka broker setup (KRaft mode)
├── producer.py           # Publishes order messages to the 'orders' topic
├── tracker.py            # Consumes and displays orders from the 'orders' topic
└── README.md
```

## Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose
- Python 3.8+
- `confluent-kafka` library

## Setup

### 1. Start Kafka

```bash
docker compose up -d
```

### 2. Install Python dependencies

```bash
pip install confluent-kafka flask
```

### 3. Create the topic

```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --create --topic orders \
  --bootstrap-server localhost:9092 \
  --partitions 1 --replication-factor 1
```

## Usage

### Produce a message

```bash
python producer.py
```

This sends a sample order (with `order_id`, `user`, `items`, `quantity`) to the `orders` topic.

### Consume messages

```bash
python tracker.py
```

This listens to the `orders` topic and prints each received order.

### Reset the topic (start fresh)

```bash
# Delete
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --delete --topic orders --bootstrap-server localhost:9092

# Recreate
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --create --topic orders \
  --bootstrap-server localhost:9092 \
  --partitions 1 --replication-factor 1
```

## Key Concepts Learned

| Concept | Description |
|---|---|
| **Topic** | A named stream of messages (e.g. `orders`) |
| **Producer** | Sends messages to a topic |
| **Consumer** | Reads messages from a topic |
| **Offset** | Position of a message in a partition |
| **Consumer Group** | Group of consumers sharing the workload |
| **KRaft mode** | Kafka without ZooKeeper (Kafka 4.x default) |

## Kafka in Docker (KRaft Mode)

This project runs Kafka in **KRaft mode** — Kafka's built-in consensus without ZooKeeper, using the `apache/kafka` official Docker image.
