#!/usr/bin/env python
# coding: utf-8

# ## Generating Prime Numbers
# 
# 
# To generate a prime number we will implement the following Algorithm. This will be useful for implementing an RSA encryption scheme or the El Gamal Scheme. 
# 
# **Generating a random prime Algorithm**
# 
# **Input**: Length n
# **Output**: A random n-bit prime
#     for $i = 1$ to $n^2/c$:
#         randomly choose a n-1 bit binary number p'
#         p := 1|p'
#         run the Miller-Rabin test on input p and parameter n
#         if the output is \prime", return p
# return fail
# 
# Note that it follows from the prime number theorem that the probability that a randomly-selected n-bit integer is prime is c/n. Therefore the the probability that a prime is not chosen in any iteration can be shown to be bounded above by e^-n. Therefore the probability of not chooseing a prime is negligble. Further the Miller-Rabin test always outputs prime if p is prime and outputs prime with negligible probability if p is composite. 
# 
# It is possible to implement the Miller-Rabin test in liner time. Therefore the above algorithm runs in polynomial time and fails to return a prime with negligble probability. 

# In[3]:


import random
from MRPrime import MRisPrime


def generatePrime(n):
    for i in range(1,(n**2)+1):
        pbar = [random.randint(0,1) for x in range(0,n-1)]
        psbar= ''.join(map(str,pbar))
        p='1'+psbar
        pcheck=int(p,2)
        if MRisPrime(pcheck,n):
            return pcheck
    return -1



# In[ ]:




