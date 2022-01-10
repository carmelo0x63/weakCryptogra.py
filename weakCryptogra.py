#!/usr/bin/env python3
# Set of functions for WEAK Cryptography
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history, date format ISO 8601:
#  2022-01-10 Added substitution cipher

def substitution(message, key, mode = 0):
    """
    The substitution cipher is a method of encrypting in which units of plaintext are replaced with the ciphertext, in a defined manner, with the help of a key.
    The receiver deciphers the text by performing the inverse substitution process to extract the original message.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''

    if mode:
        for char in message:
            try:
                output += key[alphabet.index(char)]
            except ValueError:
                output += char
    else:
        for char in message:
            try:
                output += alphabet[key.index(char)]
            except ValueError:
                output += char

    return output


def reverse(clearTxt):
    """
    The reverse cipher encrypts a message by printing it in reverse order. So 'Hello, world!' encrypts to '!dlrow ,olleH'.
    To decrypt, or get the original message, you simply reverse the encrypted message. The encryption and decryption steps are the same.
    """    

    cipherTxt = ''  # 'cipherTxt' will contain the reversed string

    for idx in range(len(clearTxt), 0, -1):
        cipherTxt += clearTxt[idx - 1]

    return cipherTxt


def caesar(clearTxt, key, mode = 0):
    """
    The Caesar cipher works by substituting each letter of a message 'clearTxt' with a new letter after shifting the alphabet over by 'key' positions. For example (e.g. key = 3), every A in the message would be replaced by a D, every B would be an E, and so on.
    When a letter at the end of the alphabet must be shifted, such as Y, it must be wrapped around to the beginning of the alphabet and shifted three places to B.
    'mode' takes two different values: 0 (default) = encrypt, 1 = decrypt.
    """

    SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'  # len(SYMBOLS) = 93
    cipherTxt = ''  # Output string

    for letter in clearTxt:
        if letter in SYMBOLS:
            letterIndex = SYMBOLS.find(letter)
#            print(f'letter: {letter}\t index: {letterIndex}')

            if mode:
                newIndex = letterIndex - key  # if 'mode' is set the request is to decrypt, that is to shift the symbols left, hence the "-"
            else:
                newIndex = letterIndex + key  # if 'mode' is NOT set (default value) the request is to encrypt, letters are shifted right, hence the "+"

            # Out of margins/wrap-around is handled here with some modulo-like logic
            if newIndex >= len(SYMBOLS):
                newIndex -= len(SYMBOLS)
            elif newIndex < 0:
                newIndex += len(SYMBOLS)

            cipherTxt += SYMBOLS[newIndex]
        else:
            cipherTxt += letter

    return cipherTxt


def columnar(message, key, mode = 0):
    """
    The transposition cipher rearranges the message’s symbols into an order that makes the original message unreadable. Each key creates a different ordering, or permutation, of the characters.
    """

    import math

    if mode:
        numOfColumns = math.ceil(len(message) / key)
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
        clearTxt = [''] * numOfColumns
        column = 0
        row = 0
        for symbol in message:
            clearTxt[column] += symbol
            column += 1
            if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                column = 0
                row += 1
        return ''.join(clearTxt)

    else:
        width = key
        cipherTxt = ''  # Output string
        for column in range(key):
            index = 0
            while index <= len(message):
                try:
                    cipherTxt += message[column + index]
                except IndexError:
                    cipherTxt += ''
                index += width
        return cipherTxt

