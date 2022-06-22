import random
import os
import socket


def recvuntil(s, delim=b'\n'):
    buf = b''
    while delim not in buf:
        buf += s.recv(1)
    return buf


def left_unshift(x, shift, mask):
    i = shift
    y = x
    while i < 32:
        y = x ^ ((y << shift) & mask)
        i += shift
    return y


def right_unshift(x, shift):
    i = shift
    y = x
    while i < 32:
        y = x ^ (y >> shift)
        i += shift
    return y


def reproduce(numbers):
    for i in range(len(numbers)):
        num = numbers[i]
        num = right_unshift(num, 18)
        num = left_unshift(num, 15, 0xefc60000)
        num = left_unshift(num, 7, 0x9d2c5680)
        num = right_unshift(num, 11)
        numbers[i] = num

    rng = random.Random()
    state = rng.getstate()
    newstate = (state[0], tuple(numbers + [624]), state[2])
    rng.setstate(newstate)
    return rng


def main():
    host = os.getenv('CTF4B_HOST', 'localhost')
    port = int(os.getenv('CTF4B_PORT', '9777'))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    recvuntil(s, b'oracle: ')
    N = -1 * (1 << (624 * 32 - 1))
    print(f'bits of N: {N.bit_length()}')
    s.send(str(N).encode() + b'\n')
    recvuntil(s, b'is: ')
    oracle = int(recvuntil(s))
    oracle ^= N

    nums = []
    for i in range(624):
        nums.append(oracle & 0xffffffff)
        oracle >>= 32

    rng = reproduce(nums)
    recvuntil(s, b'oracle: ')
    s.send(str(0xffffffff).encode() + b'\n')
    recvuntil(s, b'is: ')
    actual = int(recvuntil(s)) ^ 0xffffffff
    print(f'predict: {rng.getrandbits(32)}')
    print(f'actual: {actual}')

    recvuntil(s, b'oracle: ')
    s.send(b'\n')

    recvuntil(s, b'flag: ')
    encrypted_flag = int(recvuntil(s))

    state = rng.getstate()
    for i in range(10):
        rand = rng.getrandbits(encrypted_flag.bit_length() + i)
        flag = encrypted_flag ^ rand
        try:
            flag = bytes.fromhex(hex(flag)[2:])
            if b'ctf4b' in flag:
                print(flag.decode())
        except ValueError:
            pass
        rng.setstate(state)



if __name__ == '__main__':
    main()
