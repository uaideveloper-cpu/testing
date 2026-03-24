import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create exchange (event bus)
channel.exchange_declare(exchange='event_bus', exchange_type='fanout')

event = {
    "event": "user_created",
    "data": {
        "user_id": 1,
        "name": "Mohan"
    }
}

channel.basic_publish(
    exchange='event_bus',
    routing_key='',
    body=json.dumps(event)
)

print("Event sent!")

connection.close()