FROM resin/raspberrypi3-python:3.6

RUN apt-get update && apt-get install wakeonlan

RUN pip3 install paho-mqtt 

RUN pip3 install requests

ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV PYTHONPATH="/common"

WORKDIR /code

CMD ["python3", "hub.py"]
