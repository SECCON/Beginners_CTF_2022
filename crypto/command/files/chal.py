from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import isPrime
from secret import FLAG, key
import os


def main():
    while True:
        print('----- Menu -----')
        print('1. Encrypt command')
        print('2. Execute encrypted command')
        print('3. Exit')
        select = int(input('> '))

        if select == 1:
            encrypt()
        elif select == 2:
            execute()
        elif select == 3:
            break
        else:
            pass

        print()


def encrypt():
    print('Available commands: fizzbuzz, primes, getflag')
    cmd = input('> ').encode()

    if cmd not in [b'fizzbuzz', b'primes', b'getflag']:
        print('unknown command')
        return

    if b'getflag' in cmd:
        print('this command is for admin')
        return

    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(pad(cmd, 16))
    print(f'Encrypted command: {(iv+enc).hex()}')


def execute():
    inp = bytes.fromhex(input('Encrypted command> '))
    iv, enc = inp[:16], inp[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        cmd = unpad(cipher.decrypt(enc), 16)
        if cmd == b'fizzbuzz':
            fizzbuzz()
        elif cmd == b'primes':
            primes()
        elif cmd == b'getflag':
            getflag()
    except ValueError:
        pass


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def primes():
    for i in range(1, 101):
        if isPrime(i):
            print(i)


def getflag():
    print(FLAG)


if __name__ == '__main__':
    main()
