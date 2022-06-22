FROM python:3.10.4-alpine

EXPOSE 5555
WORKDIR /usr/src/app

RUN apk --no-cache add socat gcc g++ make libffi-dev openssl-dev \
  && pip install pycryptodome

COPY . .
CMD ["socat", "-lf", "/dev/null", "tcp-l:5555,fork,reuseaddr", "exec:./run.sh"]
