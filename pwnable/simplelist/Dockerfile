FROM ubuntu:21.04 

ENV DEBIAN_FRONTEND nointeractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install xinetd
RUN groupadd -r pwn && useradd -r -g pwn pwn

ADD build/pwn.xinetd    /etc/xinetd.d/pwn
ADD build/init.sh       /etc/init.sh
ADD build/redir.sh      /home/pwn/redir.sh
RUN chmod 550           /home/pwn/redir.sh
RUN chmod 700           /etc/init.sh
RUN chmod 1733  /tmp /var/tmp /dev/shm

ADD FLAG        /home/pwn/flag.txt
ADD files/chall /home/pwn/chall
RUN chmod 440   /home/pwn/flag.txt
RUN chmod 550   /home/pwn/chall

RUN chown -R root:pwn /home/pwn

RUN ls /home/pwn -lh

RUN service xinetd restart
