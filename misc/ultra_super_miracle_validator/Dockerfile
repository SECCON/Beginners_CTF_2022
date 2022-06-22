FROM ubuntu:21.10 

ENV DEBIAN_FRONTEND nointeractive
ENV TMPDIR /tmp

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install --fix-missing xinetd python3 python3-pip libyara-dev clang
RUN ln -sf /usr/lib/x86_64-linux-gnu/libyara.so /usr/lib/libyara.so
RUN python3 -m pip install yara-python
RUN groupadd -r misc && useradd -r -g misc misc

ADD build/misc.xinetd    /etc/xinetd.d/misc
ADD build/init.sh       /etc/init.sh
ADD build/redir.sh      /home/misc/redir.sh
RUN chmod 550           /home/misc/redir.sh
RUN chmod 700           /etc/init.sh
RUN chmod 1733  /tmp /var/tmp /dev/shm

ADD FLAG        /home/misc/flag.txt
ADD files/main.py /home/misc/main.py
ADD files/rule.yara /home/misc/rule.yara
RUN chmod 440   /home/misc/rule.yara
RUN chmod 440   /home/misc/flag.txt
RUN chmod 550   /home/misc/main.py

RUN chown -R root:misc /home/misc
 
RUN ls /home/misc -lh
RUN python3 -c "import yara"

RUN service xinetd restart
