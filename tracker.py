from confluent_kafka import Consumer
from flask import json

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-tracker',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)

consumer.subscribe(['orders'])

print("Consumer is running and subscribed to 'orders' topic...")


try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print('Error', msg.error())
            continue

        value = msg.value().decode('utf-8')
        order = json.loads(value)

        print(f"received order: {order['quantity']} x {order['items']} from {order['user']}")
except KeyboardInterrupt:
    print("Consumer is shutting down...")


finally:
    consumer.close()