#!/usr/bin/python3

import os

print(""" _     _ _       _     _     _ _        _  _   _
| |__ (_) |_ ___| |__ | |__ (_) | _____| || | | |__
| '_ \| | __/ __| '_ \| '_ \| | |/ / _ \ || |_| '_ \\
| | | | | || (__| | | | | | | |   <  __/__   _| |_) |
|_| |_|_|\__\___|_| |_|_| |_|_|_|\_\___|  |_| |_.__/

""")

print("-" * 100)
print("""
# Source Code

import os
os.environ["PAGER"] = "cat" # No hitchhike(SECCON 2021)

if __name__ == "__main__":
    flag1 = "********************FLAG_PART_1********************"
    help() # I need somebody ...

if __name__ != "__main__":
    flag2 = "********************FLAG_PART_2********************"
    help() # Not just anybody ...
""")
print("-" * 100)

os.environ["PAGER"] = "cat" # No hitchhike(SECCON 2021)

if __name__ == "__main__":
    flag1 = "ctf4b{53cc0n_15_1n_m"
    help() # I need somebody ...

if __name__ != "__main__":
    flag2 = "y_34r5_4nd_1n_my_3y35}"
    help() # Not just anybody ...