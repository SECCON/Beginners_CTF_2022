FROM ubuntu:20.04

WORKDIR /home/ctf/phisher

COPY phisher.py ./
COPY requirements.txt ./
COPY font ./font

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install socat \
                       python3 \
                       python3-pip \
                       libopencv-dev \
                       tesseract-ocr \
                       libgl1-mesa-dev

RUN pip3 install -r requirements.txt

CMD socat TCP-L:44322,fork,reuseaddr EXEC:"python3 ./phisher.py",stderr