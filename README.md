# Project 1 - Vigenere Cipher

Project 1 for FCM 741 Applied Cryptography

Uman Ranjha

Run `chmod u+x keygen encrypt decrypt crack` first. All of them are Python 3 scripts.

## How the programs work

- **keygen** - makes a random key of n bytes using Python's `secrets` library (secure randomness) and saves it as raw bytes.
- **encrypt** - adds each key byte to each file byte: `c_i = (p_i + k_(i mod n)) mod 256`. Works on any file and writes to stdout.
- **decrypt** - subtracts the key byte instead: `p_i = (c_i - k_(i mod n)) mod 256`, which gives back the exact original file.
- **crack** - finds the key length and key for `mystery.enc` and decrypts it.

## Cracking

**Key length: 37**
**Book: Tarzan of the Apes by Edgar Rice Burroughs**

I found the key length with the index of coincidence. I tried lengths 1-200, split the ciphertext into that many columns, and averaged their IC. 37 scored about 0.062 (close to English), while most other lengths were much lower. 74, 111, etc. also scored high, but those are just multiples of 37.

Then I treated each of the 37 columns like a Caesar shift. I tried all 256 key bytes and kept the one that made the column look most like English (lots of spaces and common letters). Decrypting with that key gave the full text of Tarzan of the Apes.

The mystery file itself was provided for the course, so it isn't included in this repo.
