import psycopg2

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
        hora = horaBase + datetime.timedelta(minutes=5)
        horaBase = horaBase + datetime.timedelta(minutes=5)
        temp = int(np.random.normal(8, tempMax + 1))
        payload = {
            "fecha": str(hora),
            "Temperatura": str(temp)
        }
        hielo = {
            "fecha": str(hora),
            "Capacidad": str(int(np.random.uniform(0, 11)))
        }
        client.publish('casa/cocina/nevera', json.dumps(payload), qos=0)
        print(payload)
        if int(hora.minute) % 10 == 0:
            print(hielo)
            client.publish('casa/cocina/nevera', json.dumps(hielo), qos=0)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
    sys.exit(0)


