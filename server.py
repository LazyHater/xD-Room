import paho.mqtt.client as mqtt
import subprocess
import constants
import json
import logging
# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(constants.BEACON_CONF['status_topic'])

# The callback for when a PUBLISH message is received from the server.


def execute(task):
    if isinstance(task, basestring):
        logging.info('Executing command "%s"', task)
        subprocess.check_output(task.split(' '))
    else:
        logging.info('Running function "%s"', task)


def execute_tasks(tasks):
    for t in tasks:
        execute(t)


def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    logging.info('New Event! Type %s User %s Date %s', data['type'], data['name'], data['date'])
    execute_tasks(tasks[data['type']])


tasks = {
    'ENTER': ['lamp -l 3', constants.WPC_CMD],
    'LEAVE': ['lamp -l 0'],
}

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s', datefmt='%m-%d-%Y %H:%M:%S')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect(host="127.0.0.1", port=1883, keepalive=60)
client.connect(**constants.MQTT_CON)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
