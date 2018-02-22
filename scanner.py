#!/usr/bin/python
from bluepy.btle import Scanner, DefaultDelegate
import logging
from datetime import datetime, timedelta
import paho.mqtt.publish as publish
import json
import constants


class ScanDelegate(DefaultDelegate):
    def __init__(self, user):
        DefaultDelegate.__init__(self)
        self.user = user

    def handleDiscovery(self, dev, isNewDev, isNewData):
        self.user.saw(dev.addr)
        logging.debug("Discovered device %s %s", dev.addr, dev.rssi)


class User(object):
    def __init__(self):
        self.is_present = False
        self.last_seen = datetime(1996, 4, 29)
        self.beacon_addr = constants.BEACON_CONF['mac']
        self.timeout = constants.BEACON_CONF['timeout']
        self.name = constants.BEACON_CONF['name']

    def saw(self, addr):
        if self.beacon_addr == addr:
            self.last_seen = datetime.now()
            if self.is_present == False:
                self.is_present = True
                self.enter_event()

    def check(self):
        if self.is_present and \
                datetime.now() - self.last_seen > timedelta(seconds=self.timeout):
            self.is_present = False
            self.leave_event()

    def send_event(self, type):
        payload = {
            'type': type,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'mac': self.beacon_addr,
            'name': self.name,
        }
        payload = json.dumps(payload)
        msgs = [
            {'topic': constants.BEACON_CONF['status_topic'],
                'payload': payload, 'qos': 2, 'retain': True},
            {'topic': constants.BEACON_CONF['event_topic'], 'payload': payload}
        ]
        publish.multiple(msgs, hostname=constants.MQTT_CON['host'],
                         port=constants.MQTT_CON['port'])

    def enter_event(self):
        logging.info('ENTER_EVENT mac %s', self.beacon_addr)
        self.send_event('ENTER')

    def leave_event(self):
        logging.info('LEAVE_EVENT mac %s', self.beacon_addr)
        self.send_event('LEAVE')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s', datefmt='%m-%d-%Y %H:%M:%S')

    user = User()
    scanner = Scanner().withDelegate(ScanDelegate(user))

    while True:
        scanner.scan(3)
        user.check()
