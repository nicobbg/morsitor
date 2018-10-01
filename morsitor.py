#!/usr/bin/python
"""
mortisor.py
A morse module translator
"""
import morse_encoding as ME
import sys

def translate(message, enc_fmt=ME.ITU_CODE):
    return "".join([enc_fmt.get(l.upper()) for l in message])

if __name__ == "__main__":
    try:
        encoding = sys.argv[2]
    except IndexError:
        encoding = ME.ITU_CODE
    print(translate(sys.argv[1], encoding))
