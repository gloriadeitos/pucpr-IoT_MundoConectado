import dht
import time
from machine import Pin

sensor = dht.DHT22(Pin(2))
led = Pin(4, Pin.OUT)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()
        print("Temperatura:", temp, "°C | Umidade:", umid, "%")

        if temp > 28:
            led.on()
            print("Temperatura:", temp, "°C → LED ligado")
        else:
            led.off()
            print("Temperatura:", temp, "°C → LED desligado")

    except OSError as e:
        print("Falha ao ler DHT22:", e)
        time.sleep(2)
