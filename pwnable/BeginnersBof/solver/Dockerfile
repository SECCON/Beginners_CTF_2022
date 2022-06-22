FROM python:3

RUN pip install -U pwn

WORKDIR /app
ADD . /app

ENV PWNLIB_NOTERM true

CMD ["python3", "solve.py"]
