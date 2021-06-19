# system library
import sys

# external library
import paho.mqtt.client as mqtt  # https://pypi.org/project/paho-mqtt/

'''
    Change Variabel
'''
broker_address = "broker.emqx.io"
port = 1883
topic = "same/topic"


def on_message(client, userdata, msg):
    '''
        Show Value of Data Sended
    '''
    # print(client)
    # print(userdata)
    value = msg.payload.decode("utf-8")
    print(value)


def on_connect(client, userdata, flags, rc):
    '''
        Check Status Connect with broker MQTT
    '''
    # print(client)
    # print(userdata)
    # print(flags)
    if rc == 0:
        print("broker connect\n")
    else:
        print("failed connect broker")


def mqtt_main(client):
    '''
        MQTT Setting
    '''
    client.on_connect = on_connect
    client.on_message = on_message

    print("connecting to broker")
    client.connect(broker_address, port, 60)  # connect to broker
    client.subscribe(topic)
    return client


try:
    print("Start service")
    print("to Stop service press CTRL + C\n")

    client = mqtt.Client()  # create new instance
    client = mqtt_main(client)
    client.loop_forever()
except KeyboardInterrupt:
    print("")
    print("Stop Service")
