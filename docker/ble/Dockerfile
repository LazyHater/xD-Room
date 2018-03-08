FROM don41382/rpi-python3-with-bluetooth:latest 

RUN pip3 install paho-mqtt

RUN pip3 install bluepy --upgrade 

# fix unexpected status
ADD ./btle.py  /usr/local/lib/python3.4/dist-packages/bluepy/btle.py 

ENV PYTHONPATH="/common"

WORKDIR /code

CMD ["python3", "ble.py"]

# TODO automate fix https://github.com/IanHarvey/bluepy/pull/224/commits/4dd8cc41dad8bf0b6315a1d22f68fdc46b576e63
