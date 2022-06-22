flag = "ctf4b{f%sAP$uT98Nv#FFHyrh2o+Lh0@8c9yoa98$ySoCW3rJPH3y&a83Xb}"

a = ""
b = ""
for i, c in enumerate(flag):
    if i % 3 == 0 or i % 5 == 0:
        a += c
    else:
        b += c

print(a)
print(b)


