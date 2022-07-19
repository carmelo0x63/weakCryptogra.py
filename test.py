#!/usr/bin/env python3

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = list(alphabet)
random.shuffle(key)

text = "zc'x qffy khy pfcczyp cd jydr bdh hxzyp vziufscfwc. rf xudhoa ad cuzx tdsf dkcfy!"

def encrypt(text, key):
    output = ''
    for char in text:
        try:
            output += key[alphabet.index(char)]
        except ValueError:
            output += char
    return output

for idx in range(1000000):
    print(idx, key, encrypt(text, key))
    random.shuffle(key)
    print()

