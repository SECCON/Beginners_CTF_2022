FROM python:3.10.4-alpine

EXPOSE 9777
WORKDIR /usr/src/app

RUN apk --no-cache add socat

COPY . .
CMD ["socat", "-lf", "/dev/null", "tcp-l:9777,fork,reuseaddr", "exec:./run.sh"]
