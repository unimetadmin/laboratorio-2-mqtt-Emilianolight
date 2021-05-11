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
        hora = horaBase + datetime.timedelta(seconds=1)
        horaBase = horaBase + datetime.timedelta(seconds=1)
        temp = int(np.random.uniform(0, 151))
        payload = {
            "fecha": str(hora),
            "Temperatura": str(temp)
        }

        client.publish('casa/cocina/nevera', json.dumps(payload), qos=0)
        print(payload)
        if temp >= 100:
            payload = {
                "fecha": str(hora),
                "Temperatura": str(temp),
                "Agua": "El agua ya ha hervido"
            }
            print(payload)
            client.publish('casa/cocina/nevera', json.dumps(payload), qos=0)

        time.sleep(0.5)


if __name__ == '__main__':
    main()
    sys.exit(0)
