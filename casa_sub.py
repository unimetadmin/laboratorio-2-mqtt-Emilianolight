import sys
import paho.mqtt.client
import psycopg2
import json
import _json


def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='casa/#', qos=2)


def query(sql):
    conexion = psycopg2.connect(host="localhost", user="postgres", password="relampago", database="Subscripcion")

    cur = conexion.cursor()
    cur.execute(sql)
    print("Insertado")
    # for name in cur.fetchall():
    #     print(name)


def on_message(client, userdata, message):
    print('------------------------------')
    print('topic: %s' % message.topic)
    print('payload: %s' % message.payload)
    print('qos: %d' % message.qos)
    son = message.payload
    array = str(son).split("\"")

    text = "'" + array[3]+array[5] + array[6] + array[7] + "'"
    print(text)
    sqls = "INSERT  INTO mensaje VALUES(" + text + ")"

    query(sqls)


def main():
    client = paho.mqtt.client.Client(client_id='Emiliano-subs', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='127.0.0.1', port=1883)
    client.loop_forever()


if __name__ == '__main__':
    main()

sys.exit(0)
