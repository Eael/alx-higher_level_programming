#!/usr/bin/python
# Author - Earl-Felix

for i in range(122, 96, -1):
    if i % 2 == 0:
        i = i
    else:
        i = i - 32
    print("{}".format(chr(i)), end="")
