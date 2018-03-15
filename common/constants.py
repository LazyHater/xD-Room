BEACON_CONF = {
        "mac": "a0:e6:f8:42:52:70",
        "timeout": 60,
        "name": "wakabajaszi",
        "status_topic": "klu/ble/status",
        "event_topic": "klu/ble/event",
        }

MQTT_CON = {
        "host": "127.0.0.1",
        "port": 1883,
        }

SUNRISE_API = {
        "base": "https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0",
        "lat": "51.121103",
        "lng": "17.048797",
        }

SUNRISE_URL = SUNRISE_API['base'].format(**SUNRISE_API)

PC_MAC = "C0:4A:00:77:10:0B"
WPC_CMD = "wakeonlan {mac}".format(mac=PC_MAC)

MQTT_TABLE_EFFECT_SET_TOPIC = "home/xdtable/effect/set"
MQTT_LAMP_SET_TOPIC = "home/xdlamp/set"
