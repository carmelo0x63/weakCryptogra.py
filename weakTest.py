# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random, sys
import weakCryptogra

def main():
    random.seed(42) # Set the random "seed" to a static value.

    for testNo in range(20): # Run 20 tests.
        # Generate random messages to test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # Convert the list back to a string.

        print(f'Test #{testNo + 1}: "{message[:50]}..."')

        # Check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = weakCryptogra.columnar(message, key)
            decrypted = weakCryptogra.columnar(encrypted, key + 1, 1)

            # If the decryption doesn't match the original message, display
            # an error message and quit:
            if message != decrypted:
                print(f'Mismatch with key {key} and message {message}.')
                print(f'Decrypted as: {decrypted}')
                sys.exit()

    print('Transposition cipher test passed.')

# If transpositionTest.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()

