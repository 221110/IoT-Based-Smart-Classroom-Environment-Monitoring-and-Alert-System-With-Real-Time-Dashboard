import paho.mqtt.publish as publish
import random
import time
import json

while True:
    data = {
        "temperature": random.uniform(20, 30),
        "humidity": random.uniform(40, 70),
        "air_quality": random.uniform(200, 500),
        "noise": random.uniform(30, 90)
    }
    publish.single("classroom/data", json.dumps(data), hostname="broker.hivemq.com")
    print("Data sent:", data)
    time.sleep(5)
