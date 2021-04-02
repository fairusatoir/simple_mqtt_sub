# install paho mqtt with pip

import paho.mqtt.client as mqtt #import the client1

def on_message(client,userdata, msg):
	a = msg.payload.decode("utf-8")
	print(a)

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("broker connect")
		global Connected
		Connected = True
	else:
		print("failed connect broker")

Connected = False
broker_address="broker.emqx.io" 

client = mqtt.Client() #create new instance
client.on_connect = on_connect
client.on_message = on_message

print("connecting to broker")
client.connect(broker_address,1883,60) #connect to broker
client.subscribe("test/test/cloud")

try:
	client.loop_forever()
except KeyboardInterrupt:
	print("Error");
