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
        hora = horaBase + datetime.timedelta(minutes=1)
        horaBase = horaBase + datetime.timedelta(minutes=1)
        cantPersonas = int(np.random.uniform(0, 11))
        payload = {
            "fecha": str(hora),
            "cantidad de personas": str(cantPersonas)
        }

        client.publish('casa/cocina/sala', json.dumps(payload), qos=0)
        print(payload)
        if cantPersonas > 5:
            payload = {
                "fecha": str(hora),
                "cantidad de personas": str(cantPersonas),
                "Alerta": "Demasiadas personas dentro de la habitación"
            }
            print(payload)
            client.publish('casa/cocina/sala', json.dumps(payload), qos=0)

        time.sleep(0.5)


if __name__ == '__main__':
    main()
    sys.exit(0)
