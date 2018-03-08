FROM resin/raspberrypi3-python:3.6

RUN pip3 install paho-mqtt

ENV PYTHONPATH="/common"

WORKDIR /code

CMD ["python3", "hub.py"]

#CMD ["tail", "-f", "/dev/null"]
