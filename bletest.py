from bluepy.btle import Scanner, DefaultDelegate
from datetime import datetime


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        self.is_present = False
        self.last_seen = None

    def handleDiscovery(self, dev, isNewDev, isNewData):
        self.is_present = True
        self.last_seen = datetime.now()
        if isNewDev:
            print ("Discovered device {} {}".format(dev.addr, dev.rssi))

scanner = Scanner().withDelegate(ScanDelegate())
while True:
    scanner.scan(3)

for dev in devices:
    print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    for (adtype, desc, value) in dev.getScanData():
        print "  %s = %s" % (desc, value)
