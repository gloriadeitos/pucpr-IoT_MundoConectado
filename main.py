# PUCPR
# Análise e Desenvolvimento de Sistemas
# Disciplina: Internet das Coisas em um Mundo Conectado
# Aluna: Glória Maria Deitos Gomes da Silva

from blynk import Blynk
import dht
import time
from machine import Pin

# Configuração dos componentes
sensor = dht.DHT22(Pin(2))

# LED RGB - ÂNODO COMUM (lógica invertida)
led_r = Pin(14, Pin.OUT)
led_g = Pin(27, Pin.OUT)  
led_b = Pin(26, Pin.OUT)

# Inicialmente todos OFF (para ânodo comum, OFF=1, ON=0)
led_r.on()  # Vermelho OFF
led_g.on()  # Verde OFF  
led_b.on()  # Azul OFF

# Variável para controlar o tipo de água (False=doce, True=salgada)
agua_salgada = False

# Função para processar mensagens recebidas do Blynk
def blynk_message_handler(topic, value):
    global agua_salgada
    print(f"Mensagem recebida: {topic} = {value}")
    
    if topic == "ds/Água":
        agua_salgada = (value == '1')
        print(f"Modo alterado para: {'Água Salgada' if agua_salgada else 'Água Doce'}")

# Inicializar Blynk com callback
client = Blynk(
    "Z3e7zhB0tdHKlrczTWcqX-kQoyMFHGAy",
    wifi_ssid="Wokwi-GUEST",
    wifi_password="",
    callback_func=blynk_message_handler,
    verbose=True
)

# Inscrever nos tópicos necessários
client.subscribe("downlink/ds/Água")

# Função para APAGAR todos os LEDs
def apagar_todos_leds():
    # LEDs físicos
    led_r.on()  # Vermelho OFF
    led_g.on()  # Verde OFF
    led_b.on()  # Azul OFF

# Função para controlar o LED RGB baseado na temperatura
def controlar_leds(temp):
    global agua_salgada
    
    # Primeiro APAGAR TUDO
    apagar_todos_leds()
    
    # Arredondar temperatura para número inteiro
    temp_int = int(round(temp))
    
    print(f"Temperatura analisada: {temp_int}°C | Modo: {'Salgada' if agua_salgada else 'Doce'}")
    
    # INICIALMENTE APAGA TODOS OS LEDs VIRTUAIS
    client.publish("ds/Critica", "0")
    client.publish("ds/Aceitavel", "0") 
    client.publish("ds/Ideal", "0")
    
    if agua_salgada:  # Água salgada
        if 25 <= temp_int <= 28:
            # VERDE - IDEAL
            led_g.off()  # Verde ON
            client.publish("ds/Ideal", "1")
            print(">>> VERDE ACESO - IDEAL")
        elif temp_int == 24 or temp_int == 29:
            # AZUL - ACEITAVEL  
            led_b.off()  # Azul ON
            client.publish("ds/Aceitavel", "1")
            print(">>> AZUL ACESO - ACEITAVEL")
        else:
            # VERMELHO - CRITICA
            led_r.off()  # Vermelho ON
            client.publish("ds/Critica", "1")
            print(">>> VERMELHO ACESO - CRITICA")
            
    else:  # Água doce
        if 24 <= temp_int <= 28:
            # VERDE - IDEAL
            led_g.off()  # Verde ON
            client.publish("ds/Ideal", "1")
            print(">>> VERDE ACESO - IDEAL")
        elif temp_int == 23 or temp_int == 29:
            # AZUL - ACEITAVEL
            led_b.off()  # Azul ON
            client.publish("ds/Aceitavel", "1")
            print(">>> AZUL ACESO - ACEITAVEL")
        else:
            # VERMELHO - CRITICA
            led_r.off()  # Vermelho ON
            client.publish("ds/Critica", "1")
            print(">>> VERMELHO ACESO - CRITICA")

# INICIALIZAÇÃO - GARANTIR que tudo começa APAGADO
print("=== INICIANDO - APAGANDO TODOS OS LEDs ===")
apagar_todos_leds()
client.publish("ds/Critica", "0")
client.publish("ds/Aceitavel", "0") 
client.publish("ds/Ideal", "0")
print("Todos os LEDs foram APAGADOS")
time.sleep(2)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        
        # Publicar temperatura
        client.publish("ds/Temperatura", str(temp))
        
        # Controlar LEDs
        controlar_leds(temp)
        
        time.sleep(2)
        
    except Exception as e:
        print("Erro:", e)
        time.sleep(2)
