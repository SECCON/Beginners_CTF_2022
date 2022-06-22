from random import shuffle

flag = b"ctf4b{Hey,Fox?YouCanNotTearThatHouseDown,CanYou?}"

cipher = []

for i in range(len(flag)):
    f = flag[i]
    c = (f + i)**2 + i
    cipher.append(c)

shuffle(cipher)
print("cipher =", cipher)
