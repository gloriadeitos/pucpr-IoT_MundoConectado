import network
import json
import dht
import time
from machine import Pin
from umqtt.simple import MQTTClient

sensor = dht.DHT22(Pin(2))
led = Pin(4, Pin.OUT)
LIMIAR = 28.0

SSID, PASS = "Wokwi-GUEST", ""
BROKER = "broker.emqx.io"
TOPIC = b"pucpr/iot"

w = network.WLAN(network.STA_IF); w.active(True)
w.connect(SSID, PASS)
while not w.isconnected():
    time.sleep(0.1)

cid = b"esp32-" + str(int(time.time()*1000)).encode()
c = MQTTClient(cid, BROKER)
c.connect()

while True:
    try:
        sensor.measure()
        t, u = sensor.temperature(), sensor.humidity()

        # Ascende o LED quando t >= LIMIAR
        led.value(1 if t >= LIMIAR else 0)

        # Publica somente quando o LIMIAR for atingido
        if t >= LIMIAR:
            payload = {"t": round(t,1), "u": round(u,1), "led": led.value()}
            c.publish(TOPIC, json.dumps(payload))
            print("PUB →", payload)
        else:
            print("t=", t, "u=", u, "led", led.value())

    except OSError as e:
        print("Falha ao ler DHT22:", e)
        time.sleep(2)
