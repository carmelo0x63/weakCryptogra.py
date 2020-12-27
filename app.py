#!/usr/bin/env python3
# 
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history, date format ISO 8601:
#  2020-12-07: 1.0 initial version

import argparse, sys

# Version number
__version__ = "1.0"
__build__ = "20201207"
CIPHERS = ['Caesar', 'Transposition']

def listCiphers():
    for idx in range(len(CIPHERS)):
        print('[+] ' + str(idx) + ' -> ' + CIPHERS[idx])

def main():
    parser = argparse.ArgumentParser(description='DESCRIPTION, version ' + __version__ + ', build ' + __build__ + '.')
    parser.add_argument('-c', '--cipher', metavar='Cipher', type=int)
    parser.add_argument('-l', '--list', action = 'store_true', help = 'List available ciphers')
    parser.add_argument('-k', '--key', metavar='Key', type=str)
    parser.add_argument('-f', '--file', metavar='File to en/decrypt', type=str)
    parser.add_argument('-s', '--string', metavar='String to en/decrypt', type=str)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    # In case of no arguments print help message then exits
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args() # else parse command line

    print(args) ##DEBUG

    if args.list:
        listCiphers()
        sys.exit(0)

if __name__ == '__main__':
    main()

