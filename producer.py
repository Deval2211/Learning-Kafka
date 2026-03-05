import uuid
from confluent_kafka import Producer
from flask import json

producer_config = {'bootstrap.servers': 'localhost:9092'}

producer = Producer(producer_config)

order = {
    'order_id': str(uuid.uuid4()),
    'user': 'John Doe',
    'items': 'burger',
    'quantity': 2,      
}

def dilivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered {msg.value().decode('utf-8')}")
        print(msg.topic(), msg.partition(), msg.offset())


value = json.dumps(order).encode('utf-8')

producer.produce(
    topic='orders', 
    value=value,
    callback=dilivery_report 
    )

producer.flush()