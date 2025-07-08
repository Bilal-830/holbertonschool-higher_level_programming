#!/usr/bin/python3
i = 00
while i < 100:
    print("{:02d}".format(i) , end= ", " if i != 99 else "\n" )
    i += 1
    