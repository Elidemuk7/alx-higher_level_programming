#!/usr/bin/python3
for letters in range(97, 123):
    if chr(letters) is not 'e' and chr(letters) is not 'q':
        print("{}".format(chr(letters)), end="")
