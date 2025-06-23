import os
from kafka import KafkaProducer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_MESSAGE = os.getenv("KAFKA_MESSAGE")

if not KAFKA_TOPIC or not KAFKA_MESSAGE:
    raise ValueError("Переменные окружения KAFKA_TOPIC и KAFKA_MESSAGE обязательны")

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: v.encode("utf-8")
)

producer.send(KAFKA_TOPIC, KAFKA_MESSAGE)
producer.flush()
print(f"Сообщение отправлено в топик {KAFKA_TOPIC}")
