def reverse(txt):
    """
    The reverse cipher encrypts a message by printing it in reverse order. So 'Hello, world!' encrypts to '!dlrow ,olleH'.
    To decrypt, or get the original message, you simply reverse the encrypted message. The encryption and decryption steps are the same.
    """    

    xtx = ''  # 'xtx' will contain the reversed string

    for idx in range(len(txt), 0, -1):
        xtx += txt[idx - 1]

    return xtx

def caesar(txt, key):
    pass

