# Project 1 - Vigenere Cipher

Project 1 for FCM 741 Applied Cryptography

Uman Ranjha

Four scripts, no `.py` extension. They're Python 3, so run `chmod u+x keygen encrypt decrypt crack` first. The tests run the scripts with `python3` instead, so they work even before that.

## How the programs work

- **keygen** makes a random key of n bytes with Python's `secrets` library and saves it as raw bytes.
- **encrypt** adds each key byte to each file byte: `c_i = (p_i + k_(i mod n)) mod 256`. It works on any file and writes to stdout.
- **decrypt** subtracts the key byte instead: `p_i = (c_i - k_(i mod n)) mod 256`. That gives back the exact original file.
- **crack** finds the key length and key for `mystery.enc` and decrypts it.

Arguments go `<file> <keyfile>`, in that order. The repo has 3 tests.

## Cracking

**Key length: 37**
**Book: Tarzan of the Apes by Edgar Rice Burroughs**

I found the key length with the index of coincidence. I tried lengths 1-200, split the ciphertext into that many columns, and averaged their IC. 37 scored about 0.062, close to English. Most other lengths were much lower. 74, 111, and so on also scored high, but those are just multiples of 37.

Then I treated each of the 37 columns like a Caesar shift. I tried all 256 key bytes and kept the one that made the column look most like English, lots of spaces and common letters. Decrypting with that key gave the full text of Tarzan of the Apes.

The mystery file itself was provided for the course, so it isn't included in this repo.
