from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor
import os
import socket


def recvuntil(s, delim=b'\n'):
    buf = b''
    while delim not in buf:
        buf += s.recv(1)
    return buf


def pad(b):
    n = 16 - len(b) % 16
    return b + bytes([n] * n)


plain = pad(b'primes')
target = pad(b'getflag')

host = os.getenv('CTF4B_HOST', 'localhost')
port = int(os.getenv('CTF4B_PORT', '5555'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

recvuntil(s, b'> ')
s.send(b'1\n')
recvuntil(s, b'> ')
s.send(b'primes\n')
recvuntil(s, b'command: ')
enc = bytes.fromhex(recvuntil(s).strip().decode())
iv = enc[:16]

diff = strxor(plain, target)
newiv = strxor(iv, diff)

recvuntil(s, b'> ')
s.send(b'2\n')
recvuntil(s, b'> ')
s.send((newiv + enc[16:]).hex().encode() + b'\n')
result = s.recv(1024)

print(result.decode())
s.close()
