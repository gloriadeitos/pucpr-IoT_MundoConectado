from blynk import Blynk
from servo import Servo
import time
import dht
from machine import Pin

tampa = Servo(18)
dht22 = dht.DHT22(Pin(2))
led = Pin(23,Pin.OUT)

def mensagens_recebidas(topic,value):
    if topic == "ds/LED":
        if value == "1":
            led.on()
        else:
            led.off()
    if topic == "ds/Servo":
        tampa.set_angle(int(value))

client = Blynk(
    "<TOKEN>",
    wifi_ssid="Wokwi-GUEST",
    wifi_password="",
    callback_func=mensagens_recebidas,
    verbose=True
)

client.subscribe("downlink/ds/#")

while True:
    dht22.measure()
    temp = dht22.temperature()
    umi = dht22.humidity()
    client.publish("ds/Temperatura", str(temp))
    client.publish("ds/Umidade", str(umi))
    time.sleep(1)
