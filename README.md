# Weak Cryptography
They say, (deep voice) "Never roll your own cryptography!". And that's [right](https://www.schneier.com/blog/archives/2015/05/amateurs_produc.html)!</br>
Except for one thing, how does one learn if (s)he's not allowed to make mistakes?

**WARNING**: **weak** cryptography ahead! Use `weakCryptogra.py` as a sandbox for introductory courses and experiments.

The code has been entirely rewritten but it's heavily inspired by Al Sweigart's wonderful series of books. Particularly [Cracking Codes with Python](https://inventwithpython.com/cracking/).

**Disclaimer**: the files contained herewith are clearly an implementation of **weak** cryptographic functions.</br>
Use them to try and learn as you please. **Never** use them for any serious, real-life applications!

### Usage
>>> import weakCryptogra

>>> weakCryptogra.reverse('Hello, world!')
'!dlrow ,olleH'

>>> weakCryptogra.caesar('Hello, world!', 17)
'YvCCF{ NFICu='

