FROM don41382/rpi-python3-with-bluetooth:latest 

RUN pip3 install paho-mqtt

ENV PYTHONPATH="/common"

WORKDIR /code

CMD ["python3", "ble.py"]
