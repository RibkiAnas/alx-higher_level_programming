#!/usr/bin/python3
def uppercase(str):
    for i in range(97, 123):
        str = str.replace(chr(i), chr(i -32))
    print(str)
