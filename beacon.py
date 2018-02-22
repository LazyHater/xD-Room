#!/usr/bin/python
from bluepy.btle import Scanner, DefaultDelegate
from datetime import datetime, timedelta
import subprocess
import os
import sys
import logging


class ScanDelegate(DefaultDelegate):
    def __init__(self, user):
        DefaultDelegate.__init__(self)
        self.user = user

    def handleDiscovery(self, dev, isNewDev, isNewData):
        user.saw(dev.addr)
        logging.debug("Discovered device %s %s", dev.addr, dev.rssi)


class User(object):
    def __init__(self):
        self.is_present = False
        self.last_seen = datetime(1996, 4, 12)
        self.beacon_addr = 'a0:e6:f8:42:52:70'
        self.pc_addr = '00:22:15:ae:48:89'
        self.timeout = 60
        self.lamp_lv_on_enter = 3
        self.lamp_lv_on_leave = 0

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

    def enter_event(self):
        logging.info('ENTER_EVENT')
        logging.info('Setting lamp to level %s', self.lamp_lv_on_enter)
        subprocess.check_output(['lamp', '-l', str(self.lamp_lv_on_enter)])
        logging.info(subprocess.check_output(['sudo', 'wakeonlan', self.pc_addr]).strip())

    def leave_event(self):
        logging.info('LEAVE_EVENT')
        logging.info('Setting lamp to level %s', self.lamp_lv_on_leave)
        subprocess.check_output(['lamp', '-l', str(self.lamp_lv_on_leave)])
        logging.info('Putting pc to sleep ;-)')
        return
        try:
            resp = subprocess.check_output(['ssh', 'pc', 'sudo', 'systemctl', 'suspend'])
        except subprocess.CalledProcessError:
            logging.error('Unable to connect to pc!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s', datefmt='%m-%d-%Y %H:%M:%S')

    user = User()
    scanner = Scanner().withDelegate(ScanDelegate(user))

    while True:
        scanner.scan(3)
        user.check()
