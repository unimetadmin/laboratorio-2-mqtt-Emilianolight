import requests
import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime


def on_connect(client, userdata, flags, rc):
    print('conectado publicador')


def main():
    client = paho.mqtt.client.Client("Emiliano", False)
    client.qos = 0
    client.connect(host='127.0.0.1')
    meanEntrada = 10
    stdEntrada = 2
    tempMax = 12
    horaBase = datetime.datetime.now().replace(minute=0, second=0)
    personasPorHora = np.random.normal(meanEntrada, stdEntrada)
    horaBase = horaBase + datetime.timedelta(hours=1)

    while True:
        hora = horaBase + datetime.timedelta(minutes=30)
        horaBase = horaBase + datetime.timedelta(minutes=30)

        url = "http://api.openweathermap.org/data/2.5/weather?q=Caracas&appid=6cf9ae43293928ec740fd51b2c9c524a"
        data = requests.get(url).json()

        temp = int(data['main']['temp']) - 273

        payload = {
            "fecha": str(hora),
            "Temperatura de Caracas ": str(temp)
        }

        client.publish('casa/cocina/sala', json.dumps(payload), qos=0)
        print(payload)

        time.sleep(0.5)


if __name__ == '__main__':
    main()
    sys.exit(0)
