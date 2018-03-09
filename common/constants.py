BEACON_CONF = {
        "mac": "a0:e6:f8:42:52:70",
        "timeout": 15,
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

LAMP_ON_CMD="curl -s --data level=3 http://192.168.1.9/lamp"
LAMP_OFF_CMD="curl -s --data level=0 http://192.168.1.9/lamp"

