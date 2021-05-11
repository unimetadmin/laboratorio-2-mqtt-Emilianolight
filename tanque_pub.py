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
    capacidad = 100
    horaBase = datetime.datetime.now().replace(minute=0, second=0)
    personasPorHora = np.random.normal(meanEntrada, stdEntrada)
    horaBase = horaBase + datetime.timedelta(hours=1)

    while True:
        hora = horaBase + datetime.timedelta(minutes=10)
        horaBase = horaBase + datetime.timedelta(minutes=10)
        if int(hora.minute) == 0 or int(hora.minute) == 30:
            capacidad += int(np.random.uniform(20, 5))

        capacidad -= int(np.random.uniform(10, 5))
        payload = {
            "fecha": str(hora),
            "Nivel del tanque ": str(capacidad)
        }
        if capacidad <= 0:
            capacidad = 0
        payload = {
            "fecha": str(hora),
            "Nivel del tanque ": str(capacidad)
        }
        client.publish('casa/cocina/baño', json.dumps(payload), qos=0)
        if capacidad <= 0:
            capacidad = 0
            payload = {
                "fecha": str(hora),
                "cantidad de personas": str(capacidad),
                "Alerta": "Tanque vacío"

            }
            print(payload)
            client.publish('casa/cocina/baño', json.dumps(payload), qos=0)
            print(payload)

        elif capacidad <= 50:
            payload = {
                "fecha": str(hora),
                "cantidad de personas": str(capacidad),
                "Alerta": "Queda menos de la mitad del agua"

            }
        print(payload)
        client.publish('casa/cocina/baño', json.dumps(payload), qos=0)
        time.sleep(0.5)




if __name__ == '__main__':
    main()
    sys.exit(0)
