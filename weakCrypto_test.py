import unittest
import weakCryptogra
import random

class weakTest(unittest.TestCase):
    def test_columnar(self):

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
                decrypted = weakCryptogra.columnar(encrypted, key, 1)

                self.assertEqual(decrypted, message)

if __name__ == '__main__':
    unittest.main()

