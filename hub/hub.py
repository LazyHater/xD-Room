import paho.mqtt.client as mqtt
import subprocess
import constants
import json
import logging
import sunrise
import datetime
import threading
# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(constants.BEACON_CONF['status_topic'])

# The callback for when a PUBLISH message is received from the server.


def execute(task):
    if isinstance(task, str):
        logging.info('Executing command "%s"', task)
        subprocess.check_output(task.split(' '))
    elif callable(task):
        logging.info('Running function "%s"', task)
        task()
    else:
        logging.error("Unknown command type: %s", task)

def execute_tasks(tasks):
    for t in tasks:
        execute(t)


def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    logging.info("")
    logging.info('New Event! Type %s User %s Date %s', data['type'], data['name'], data['date'])
    execute_tasks(tasks[data['type']])


def lamp_enter_handler():
    is_day = False
    try:
        partial = sunrise.get_sunrise_and_sunset(constants.SUNRISE_URL)
        logging.debug("Sunrise at %s sunset at %s now is %s", *partial, datetime.datetime.utcnow())
        is_day = sunrise.is_day_now(*partial)
    except Exception as e:
        logging.error("Failed to determine is_day, asssume night!%s", e)
    if not is_day:
        execute(constants.LAMP_ON_CMD)


# egz { {"color": {"r": 255, "b": 455, "g": 455}, }}
def set_table_effect(idx):
    payload = {
        'idx': idx,
    }
    payload = json.dumps(payload)

    client.publish("klu/table/effect", payload)

def table_enter_handler():
    set_table_effect(6) # disco

    t = threading.Timer(60, set_table_effect, args=(3,)) # sin2
    t.start()

def table_leave_handler():
    set_table_effect(11) # black

client = mqtt.Client()

if __name__ == "__main__":
    tasks = {
            'ENTER': [ lamp_enter_handler, table_enter_handler, constants.WPC_CMD],
            'LEAVE': [ constants.LAMP_OFF_CMD, table_leave_handler],
    }

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s', datefmt='%m-%d-%Y %H:%M:%S')


    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(**constants.MQTT_CON)
    client.loop_forever()
