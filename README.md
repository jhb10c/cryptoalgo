# cryptoalgo
This Repo contains implementations of (non-production) cryptographic schemes and primitives.

The primenumbergenerator folder contains two algorithms: Miller-Rabin Test and a Prime Number generator. 

1. Interactive with the Miller-Rabin Test: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jhb10c/cryptoalgo/main?filepath=PrimeNumberGenerator%2FMRPrime.ipynb)

2. Generate a random prime number up to 32 bits length in under a minute. Note that this uses random.randint. This is not a true source of randomness. Therefore the primes appear random but are actually not. This algorithm would produce a truly random prime if random.randint is replaced with a source of true randomness: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jhb10c/cryptoalgo/main?filepath=PrimeNumberGenerator%2FPrimeNumberGenerator.ipynb)

The vigenere folder contains two files: An implementation of the encryption/decryption of the vigenere cipher and an attack on the vigenere cipher that completely recovers the private key for sufficently large messages. This attack on the vigenere cipher is a programming assignment from Dr. John Katz's coursera course "Cryptography".

3. Encrypt and Decrypt with the Vigenere scheme: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jhb10c/cryptoalgo/main?filepath=vigenere%2FLAB2Sols.ipynb)

4. An Attack on the Vigenere Cipher: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jhb10c/cryptoalgo/main?filepath=vigenere%2FBvigenerecipher.ipynb)


