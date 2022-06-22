FROM ubuntu:21.04

ENV DEBIAN_FRONTEND nointeractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade --fix-missing
RUN apt-get install -y gcc make build-essential

CMD make -C /build chall
