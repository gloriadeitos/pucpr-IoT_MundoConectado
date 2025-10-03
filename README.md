#### Glória Maria Deitos Gomes da Silva <br> 22.Junho.2025

# pucpr-iot-connected-world

<p align="center">
  <img src="https://github.com/gloriadeitos/gloriadeitos/blob/main/img/pucpr.png" alt="ufpr" height="100">
  <img src="https://github.com/gloriadeitos/gloriadeitos/blob/main/img/octacore.png" alt="octacore" height="100">
  <img src="https://github.com/gloriadeitos/gloriadeitos/blob/main/img/gloriadeitos-logo.png" alt="gloriadeitos-logo" height="100">
</p>

**Disciplina:** Internet das Coisas em um Mundo Conectado <br>
**Curso:** Análise e Desenvolvimento de Sistemas <br>
**Instituição:** Pontifícia Universidade Católica do Paraná (PUCPR) - Brasil  

## 📋 Sobre o Projeto

Este repositório contém os projetos desenvolvidos durante a disciplina de Internet das Coisas em um Mundo Conectado, utilizando simuladores como Wokwi, protocolos MQTT, integração com plataformas IoT como Blynk, e programação em MicroPython para ESP32.

## 🛠️ Tecnologias Utilizadas

- **Microcontrolador:** ESP32
- **Linguagem:** MicroPython
- **Simulador:** Wokwi
- **Protocolo de Comunicação:** MQTT
- **Plataforma IoT:** Blynk
- **Cliente MQTT:** MQTTX
- **Frontend:** HTML/CSS/JavaScript

## 📁 Estrutura do Projeto

```
📦 pucpr-IoT_MundoConectado
├── 📄 README.md
├── 📄 index.html                    # Interface web principal
├── 📄 main.py                       # Código principal do projeto
├── 📄 blynk.py                      # Biblioteca para integração com Blynk
├── 📄 umqttsimple.py               # Biblioteca MQTT simplificada
├── 📄 diagram.json                  # Diagrama do circuito Wokwi
├── 🖼️ esp32.png                     # Imagem do ESP32
├── 🖼️ aquarium.webp                # Imagem do aquário
├── 🖼️ bg.jpg                        # Imagem de fundo
├── 📄 Somativa2-IoT_MundoConectado-GloriaDeitos.pdf
├── 📁 Videoaula01-Introducao_ao_Wokwi/
│   ├── 📄 diagram.json
│   └── 📄 main.py
├── 📁 Videoaula02-Integracao_Wokwi_MQTTX/
│   ├── 📄 diagram.json
│   ├── 📄 main.py
│   ├── 📄 umqttsimple.py
│   └── 📁 estacao-metereologica/
│       ├── 📄 blynk.py
│       ├── 📄 diagram.json
│       ├── 📄 main.py
│       ├── 📄 servo.py
│       ├── 📄 umqttsimple.py
│       └── 📄 wokwi-project.txt
└── 📁 Videoaula03-Intregracao_com_Blynk/
    └── 📄 main.py
```

## 🎯 Objetivos de Aprendizagem

- Compreender os conceitos fundamentais de IoT
- Desenvolver projetos práticos com ESP32 e MicroPython
- Implementar comunicação MQTT entre dispositivos
- Integrar sensores e atuadores em projetos IoT
- Utilizar plataformas de nuvem para monitoramento e controle
- Criar interfaces web para interação com dispositivos IoT

## 📚 Videoaulas e Projetos

### 🎥 Videoaula 01 - Introdução ao Wokwi
- **Objetivo:** Primeiros passos com o simulador Wokwi
- **Tecnologias:** ESP32, MicroPython, Wokwi
- **Arquivos:** `Videoaula01-Introducao_ao_Wokwi/`

### 🎥 Videoaula 02 - Integração Wokwi + MQTTX
- **Objetivo:** Implementação de comunicação MQTT
- **Projeto Especial:** Estação Meteorológica
- **Tecnologias:** MQTT, MQTTX, Sensores
- **Arquivos:** `Videoaula02-Integracao_Wokwi_MQTTX/`

#### 🌡️ Estação Meteorológica
Projeto completo de uma estação meteorológica com:
- Sensores de temperatura e umidade
- Controle de servo motor
- Comunicação MQTT
- Integração com Blynk

### 🎥 Videoaula 03 - Integração com Blynk
- **Objetivo:** Controle e monitoramento via aplicativo Blynk
- **Tecnologias:** Blynk IoT Platform, ESP32
- **Arquivos:** `Videoaula03-Intregracao_com_Blynk/`

## 🚀 Como Executar os Projetos

### Pré-requisitos
- Conta no [Wokwi](https://wokwi.com/)
- Conta no [Blynk](https://blynk.io/)
- Cliente MQTT (MQTTX recomendado)
- Navegador web moderno

### Passos para Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gloriadeitos/pucpr-IoT_MundoConectado.git
   cd pucpr-IoT_MundoConectado
   ```

2. **Acesse o Wokwi e crie um novo projeto**

3. **Copie o código do arquivo `main.py` desejado**

4. **Importe o diagrama do circuito (`diagram.json`)**

5. **Configure as credenciais necessárias:**
   - WiFi SSID e senha
   - Broker MQTT
   - Token do Blynk (quando aplicável)

6. **Execute a simulação no Wokwi**

## 📊 Principais Funcionalidades

- ✅ Simulação de dispositivos IoT
- ✅ Comunicação MQTT
- ✅ Integração com Blynk
- ✅ Controle de sensores e atuadores
- ✅ Interface web responsiva
- ✅ Monitoramento em tempo real
- ✅ Estação meteorológica completa

## 🔧 Configurações Importantes

### MQTT
```python
MQTT_BROKER = "broker.hivemq.com"  # ou seu broker preferido
MQTT_PORT = 1883
MQTT_TOPIC = "seu/topico/aqui"
```

### WiFi
```python
WIFI_SSID = "SeuWiFi"
WIFI_PASSWORD = "SuaSenha"
```

### Blynk
```python
BLYNK_AUTH = "SeuTokenBlynk"
```

## 📈 Resultados e Aprendizados

- Desenvolvimento de habilidades em programação IoT
- Compreensão de protocolos de comunicação
- Experiência prática com simuladores
- Integração de hardware e software
- Criação de interfaces de usuário para IoT

## 🤝 Contribuições

Este é um projeto acadêmico individual, mas sugestões e melhorias são sempre bem-vindas!

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

**Glória Maria Deitos Gomes da Silva**
- 📧 Email: [seu-email@exemplo.com]
- 💼 LinkedIn: [linkedin.com/in/gloriadeitosdev](https://linkedin.com/in/gloriadeitosdev)
- 🐱 GitHub: [@gloriadeitos](https://github.com/gloriadeitos)

---

<p align="center">
  Desenvolvido com ❤️ durante a disciplina de IoT na PUCPR
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ESP32-000000?style=for-the-badge&logo=espressif&logoColor=white">
  <img src="https://img.shields.io/badge/MicroPython-2B2728?style=for-the-badge&logo=micropython&logoColor=white">
  <img src="https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=eclipse-mosquitto&logoColor=white">
  <img src="https://img.shields.io/badge/Wokwi-4CAF50?style=for-the-badge&logo=wokwi&logoColor=white">
  <img src="https://img.shields.io/badge/Blynk-00C7B7?style=for-the-badge&logo=blynk&logoColor=white">
</p>
