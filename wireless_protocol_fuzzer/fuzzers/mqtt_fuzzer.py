import paho.mqtt.client as mqtt
import random
from utils.logger import log

def fuzz_mqtt():
    client = mqtt.Client()

    try:
        client.connect("localhost", 1883, 60)

        for i in range(50):
            payload = bytes([random.randint(0,255) for _ in range(10)])
            client.publish("fuzz/topic", payload)
            log(f"MQTT fuzz iteration {i}")

        client.disconnect()

    except Exception as e:
        log(f"MQTT Error: {e}")