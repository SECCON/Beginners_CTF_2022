FROM python:3.10.4-alpine

WORKDIR /usr/src/app
RUN apk --no-cache add socat gcc g++ make libffi-dev openssl-dev \
  && pip install pycryptodome
COPY . .

CMD ["python", "solve.py"]
