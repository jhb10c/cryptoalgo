#!/usr/bin/env python
# coding: utf-8

# ## Vigenere Cipher
# 
# The vigenere cipher is a private key encryption scheme.  
# 
# The encryption algorithm and decryption algorithm are identical. We will describe the encryption algorithm. It take two inputs: a message and a key. To encrypt the message with the key, each charactor of the message is XORed with a character of the key sequentially. If the key is shorter then the message then they encryption wraps around back to the beginning of the key. If the key length is equal to the message length then the encryption algorithm agrees with the one-time pad.
# 
# The vigenere cipher in general is not perfectly secure. We show how to attack the vigenere cipher in the file called Lab 2. Note, when the key length is equal to the message length, then the vigenere cipher is perfectly secret. 
# 
# Below we implement the Encryption/Decryption Algorithm.

# In[ ]:


def chartoint(message):
    """converts ascii string to corresponding list of integers
    input: a string of ascii characters
    ouput: a list of the corresponding integer representation
    """
    chex = []
    for i in range(0,len(message)):
        # ord is a function that takes an ascii character and returns decimal form 
        chex.append(ord(message[i]))
    return chex


def inttochar(message):
    """converts list of integers to corresponding ascii string
    input: a list of the corresponding integer representation
    ouput:  a string of ascii characters
    """
    hold = ''
    for i in message:
        # chr is a function that takes a decimal character and returns ascii form 
        hold=hold + chr(i)
    return hold



def rotate(lista,n):
    """This function shifts a string by n characters
    input: a list of integers 
    ouput: the list of integers have been shifted to the right by n"
    """
    return lista[n:]+lista[:n]


def vigenere(message,key):
    """vigenere encryption/decryption algorithm
    inputs: message - the message that we wish to encrypt/decrypu must be a string
            key - the key used to encrypt/decrypt. must be a string
    output: cipher text / decrypted cipher
    
    """
    m=chartoint(message)
    k=chartoint(key)
    hold = [] 
    for i in m:
        hold.append(i^k[0])
        key=rotate(k,1)
    return inttochar(hold) 

#vigenere('hello','a')
#vigenere('\t\x04\r\r\x0e','a')

