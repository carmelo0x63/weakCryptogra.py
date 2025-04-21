# Weak Cryptography
They say, (deep voice) "Never roll your own cryptography!". And that's [right](https://www.schneier.com/blog/archives/2015/05/amateurs_produc.html)!</br>
Except for one thing, how does one learn if (s)he's not allowed to make mistakes?

**WARNING**: **weak** cryptography ahead! Use `weakCryptogra.py` as a sandbox for introductory courses and experiments.

The code has been entirely rewritten but it's heavily inspired by Al Sweigart's wonderful series of books. Particularly [Cracking Codes with Python](https://inventwithpython.com/cracking/).<br/>
The repository stores a copy of [CrackingCodesFiles.zip](https://inventwithpython.com/CrackingCodesFiles.zip) from the same website.<br/>

**Disclaimer**: the files contained herewith are clearly an implementation of **weak** cryptographic functions.</br>
Use them to try and learn as you please. **Never** use them for any serious, real-life applications!

### Usage
```
>>> import weakCryptogra
```

#### Reverse cipher
```
>>> weakCryptogra.reverse('Hello, world!')
'!dlrow ,olleH'
```

#### Ceeasar cipher
```
>>> weakCryptogra.caesar('Hello, world!', 17)
'YvCCF, NFICu!'
```

#### Caesar cipher: xample of brute-force decryption
```
for INDEX in range(1,27):
    print(f"{INDEX}: ", end = "")
    print(weakCryptogra.caesar('YvCCF, NFICu!', INDEX, mode = 1))
...
17: Hello, world!
...
```

#### Other examples
```
>>> weakCryptogra.columnar('Hello, world!', 3)
'Hl r!eowll,od'

>>> import random
>>> alphabet = 'abcdefghijklmnopqrstuvwxyz'
>>> key = list(alphabet)
>>> random.shuffle(key)
>>> key
['d', 'q', 'u', 't', 'n', 'w', 'g', 'k', 'm', 'o', 'c', 'f', 'y', 's', 'x', 'p', 'j', 'e', 'b', 'z', 'r', 'a', 'v', 'l', 'h', 'i']
>>> weakCryptogra.substitution('Hello!', key)
'Hrxxj!'
>>> weakCryptogra.substitution('Hrxxj!', key, 1)
'Hello!'
```

