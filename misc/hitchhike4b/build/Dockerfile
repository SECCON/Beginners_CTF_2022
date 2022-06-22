FROM python:3.10-alpine

RUN apk --no-cache add socat
RUN adduser -D ctf

ADD app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py /home/ctf/hitchhike4b/app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py
RUN chmod 500 /home/ctf/hitchhike4b/app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py
RUN chown ctf:root /home/ctf -R

USER ctf
WORKDIR /home/ctf/hitchhike4b/
CMD socat TCP-L:55433,fork,reuseaddr EXEC:"python3 ./app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py",stderr