from Crypto.Util.number import *
from flag import flag

p, q, r = getPrime(512), getPrime(256), getPrime(256)
n = p * q * r
phi = (p - 1) * (q - 1) * (r - 1)
e = 2003
d = inverse(e, phi)

flag = bytes_to_long(flag.encode())
cipher = pow(flag, e, n)

s = d % ((q - 1)*(r - 1)) & (2**470 - 1)

assert q < r
print("rq =", r % q)

print("e =", e)
print("n =", n)
print("s =", s)
print("cipher =", cipher)
