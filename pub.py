import paho.mqtt.publish as publish

msgs = [
{'topic':"bene/ble/status", 'payload':"ENTER", 'qos': 2, 'retain': True},
{'topic':"bene/ble/events", 'payload':"ENTER"}]
publish.multiple(msgs, hostname="192.168.1.10")
