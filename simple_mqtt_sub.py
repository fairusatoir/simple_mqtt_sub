# install paho mqtt with pip

import paho.mqtt.client as mqtt #import the client1
import MySQLdb


db = MySQLdb.connect("34.87.126.16","rootpy","","python_conn")
insertrec = db.cursor()

def on_message(client,userdata, msg):
	value = msg.payload.decode("utf-8").split("-")
	
	queryInsert = "INSERT INTO "+value[0]+" VALUES ("+ value[1] +",CURRENT_TIMESTAMP())"
	insertrec.execute(queryInsert)
	db.commit()
	print(queryInsert)

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
client.subscribe("delivery/py")

try:
	client.loop_forever()
except KeyboardInterrupt:
	db.close()
	print("")
	print("Close")
