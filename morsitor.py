#!/usr/bin/python
"""
mortisor.py
A morse module translator
"""
import argparse
import morse_encoding as ME
import sys


def _load_enc(name):
    '''load encoding format from the morse encoding module'''
    if name not in ['ITU_CODE', 'AMERICAN']:
        raise ValueError("Unknown encoding format")
    if name == 'ITU_CODE':
        return ME.ITU_CODE
    if name == 'AMERICAN':
        return ME.AMERICAN


def _list_format():
    '''list all available formats'''
    print("""ITU_CODE: Internation encoding
AMERICAN: American encoding
"""
          )


def translate(message, enc_fmt=ME.ITU_CODE):
    return "".join([enc_fmt.get(l.upper()) for l in message])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A morse translator\
                                                  application')
    parser.add_argument('-m', '--message',
                        dest='message',)
    parser.add_argument('-e', '--encoding',
                        help='encoding format',
                        dest='enc_fmt',
                        default='ITU_CODE'
                        )
    parser.add_argument('-l', dest="list_fmt",
                        action='store_true',
                        help='print available encoding format')
    args = parser.parse_args()

    if args.list_fmt:
        _list_format()
        sys.exit(0)

    enc = _load_enc(args.enc_fmt)
    print(translate(args.message, enc))
