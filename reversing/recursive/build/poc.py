import random

table = ["a"] * 512

for i in range(len(table)):
    t = random.choice([random.randrange(33, 65), random.randrange(95, 126)])
    table[i] = chr(t)

flag = "ctf4b{r3curs1v3_c4l1_1s_4_v3ry_u53fu1}"


def check(flag, n):
    if len(flag) == 1:
        table[n] = flag
        print(n)
    else:
        t = len(flag) // 2
        check(flag[:t], n)
        check(flag[t:], n + t**2)


check(flag, 0)

with open("table.txt", mode="w") as f:
    f.write(str(table))
