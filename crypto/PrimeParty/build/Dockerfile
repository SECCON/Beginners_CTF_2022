FROM python:3.9.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


RUN apt-get update \
    && apt-get install -y \
    socat

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY server.py /usr/src/app
COPY secret.py /usr/src/app

CMD [ "socat", "TCP-LISTEN:1336,fork,reuseaddr", "EXEC:\"python3 server.py\"" ]
