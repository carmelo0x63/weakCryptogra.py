def reverse(txt):
    """
    The reverse cipher encrypts a message by printing it in reverse order. So 'Hello, world!' encrypts to '!dlrow ,olleH'.
    To decrypt, or get the original message, you simply reverse the encrypted message. The encryption and decryption steps are the same.
    """    

    xtx = ''  # 'xtx' will contain the reversed string

    for idx in range(len(txt), 0, -1):
        xtx += txt[idx - 1]

    return xtx

def caesar(txt, key, mode = 0):
    """
    The Caesar cipher works by substituting each letter of a message 'txt' with a new letter after shifting the alphabet over by 'key' positions. For example (e.g. key = 3), every A in the message would be replaced by a D, every B would be an E, and so on.
    When a letter at the end of the alphabet must be shifted, such as Y, it must be wrapped around to the beginning of the alphabet and shifted three places to B.
    'mode' takes two different values: 0 (default) = encrypt, 1 = decrypt.
    """

    SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'  # len(SYMBOLS) = 93
    xtx = ''  # Output string

    for letter in txt:
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

            xtx += SYMBOLS[newIndex]
        else:
            xtx += letter

    return xtx

def columnar(txt, key, mode = 0):
    """
    The transposition cipher rearranges the message’s symbols into an order that makes the original message unreadable. Each key creates a different ordering, or permutation, of the characters.
    """

    import math

    if mode:
        numOfColumns = math.ceil(len(txt) / key)
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(txt)
        plaintext = [''] * numOfColumns
        column = 0
        row = 0
        for symbol in txt:
            plaintext[column] += symbol
            column += 1
            if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                column = 0
                row += 1
        return ''.join(plaintext)

    else:
        width = key
        xtx = ''  # Output string
        for column in range(key):
            index = 0
            while index <= len(txt):
                try:
                    xtx += txt[column + index]
                except IndexError:
                    xtx += ''
                index += width
        return xtx

