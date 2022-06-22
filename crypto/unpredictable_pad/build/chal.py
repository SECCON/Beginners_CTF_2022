import random
import os


FLAG = os.getenv('FLAG', 'notflag{this_is_sample_flag}')


def main():
    r = random.Random()

    for i in range(3):
        try:
            inp = int(input('Input to oracle: '))
            if inp > 2**64:
                print('input is too big')
                return

            oracle = r.getrandbits(inp.bit_length()) ^ inp
            print(f'The oracle is: {oracle}')
        except ValueError:
            continue

    intflag = int(FLAG.encode().hex(), 16)
    encrypted_flag = intflag ^ r.getrandbits(intflag.bit_length())
    print(f'Encrypted flag: {encrypted_flag}')


if __name__ == '__main__':
    main()
