#!/usr/bin/env python
# coding: utf-8

# ## Miller-Rabin Primality Test
# 
# The Miller-Rabin algorithm is an algorithm that determines whether a given number is prime. The basis of the algorithm is dependent on the observation that if $N$ is prime then $|Z_N^*|=N-1$, and so for any
# number in $|Z_N^*|$ we have $a^{N-1} = 1 mod N$. Necessarily, a given integer N is prime if  $a^{N-1} = 1 mod N$ for all $a$ in $|Z_N^*|$. On the other hand, a given integer N is composite if there exists an $a$ such that  $a^{N-1} \neq 1 mod N$. An element $a\in Z_N$ such that  $a^{N-1} \neq 1 mod N$ is called a witness that N is composite, shortened to be witness.
# 
# To test whether a given integer N is prime, the Miller-Rabin algorithm chooses a random element and determines if it is a witness. The best case scenario is that if N is not prime then there is a large probability that a random element is a witness. The following can be shown.
# 
# **Lemma.** Fix N. Say there exists a witness that N is composite. Then at least half the elements of $ Z_N^*$ are witnesses that N is composite.
# 
# However, there are infinitely-many composite numbers N that do not have any witnesses! 
# 
# 
# 
# 

# Before we implement the Miller-Rabin Primality Test, we will implement an Algorithm for modular exponentiation that runs in polynomial time with respect to the length of the exponent represented as a binary number. 
# 
# We are assuming addition, multiplication, and division runs in linear time when constructing our instance of this algorithm. 
# 
# **Algorithm Name**: ModExp
# 
# **input**: $a,b,N$
# 
# **output**: $a^b mod N$
# 
# ModExp(a,b,N):
# 
# if b =1 then return a
# else
# 
#       if b is even
#          t = ModExp(a,b/2,N)
#          return $t^2 mod N$
#       if N is odd
#          t =ModExp(a,(b-1)/2,N)
#          return $a*t^2 mod N$
#   
# 
# 

# In[101]:


def modExp(a,b,N):
    if b ==1:
        return a
    else: 
        if b%2 ==0:
            t = modExp(a,int(b/2),N)
            return t**2 % N
        if b%2 ==1:
            t = modExp(a,int((b-1)/2),N)
            return a*t**2 % N

modExp(11,2,15)
modExp(29,100,35)
modExp(3,560,561)


# ## Problem 1 
# 
# Construct a function that determines whether $a\in Z_N^*$ is a witness given $N$.
# 

# In[99]:


def isWitness(a,N):
    check = modExp(a,N-1,N)
    if check == 1:
        return False
    if check != 1:
        return True
isWitness(2,6)


# ## Problem 2 
# 
# Further, if there exists a non-identity element of $a\in Z_N$ that is not an element of $Z_N^*$ then $N$ is not prime. Construct a function that determines whether $a\in Z_N$ is an element of $a\in Z_N^*$.
# 

# In[349]:


def RGCD(a,b): 
    if a%b == 0:
        return b
    else:
        return RGCD(b,a%b)
    
def isMultiplicative(a,N):
    check = RGCD(a,N)
    if check == 1 :
        return True
    if check !=1:
        return False 
    
isMultiplicative(2,6)


# We will now assume the numbers less then N that we need to test are coprime with N. Otherwise, N is not prime.  

# ## Refining Witnesses
# 
# Let $N - 1 = 2^ru$ where u is odd and $r \geq 1$. Previously we tested for witnesses of the form $a^{N-1} = a^{2^r u}$. For the sequence of terms $(a^u, a^{2u}, \ldots a^{2^ru})$, if there exists a term a^{2^iu} equal to 1,-1 then $a^{N-1}=1$. A stronger version of witness testing would check if a term equal to either to 1,-1 does not exist in the sequence. 
# 
# We say that $a \in Z_N^*$ is a strong witness that N is composite (or simply a strong witness) if $a^{u}\neq \pm 1 mod N$ and $a^{2^{i}u}\neq -1 mod N$ for all $\{1,\ldots,  r-1\}.$ 
# 
# Note that if $a$ is not a strong witness then $a$ is not a witness. Conversely if $a$ is a witness then it is a strong witness. Further note that when an element $a$ is not a strong witness then the sequence $(a^u, a^{2u}, \ldots a^{2^ru})$, takes the following forms: $(\pm 1, 1, \ldots,  1)$ or $(*,\ldots,*,- 1, 1, \ldots , 1)$ where $*$ denotes an arbitrary term.
# 
# The following two lemmas can be shown for strong witnesses.
# 
# **Lemma.** If N is a prime then there is no strong witness for N.
# 
# 
# **Lemma.** Let N be an odd, composite number that is not a prime
# power. Then at least half the elements of $ Z_N^*$ are strong witnesses that N is composite.
# 
# 
# 

# ## Problem 3
# 
# Construct a function that determines whether $a\in Z_N^*$ is a strong witness given $N$.
# 

# In[476]:


def highestpowerof2(even):
    beven = bin(even)[2:]
    for i in range(-1, -len(beven)-1,-1):
        if beven[i] =='1':
            return -i-1
        

def isStrongWitness(a,N):
    #We are assuming N is Odd 
    #Testing Primality is Easy for Odd Numbers
    if N% 2 == 0:
        return False
    else:
        r = highestpowerof2(N-1)
        u = (N-1)/(2**r)
        #print(u)
        for i in range(0,r):
            apower = modExp(a,(2**i)*u,N)
            #print(r,u,apower)
            if i == 0 :
                if apower == 1 or  apower == N-1:
                    #print("hello1")
                    return False
            if i >=1:
                if apower == N-1:
                    #print("hello2")
                    return False
            
    return True



# As you can see for 561, there are plenty of numbers that are not witnesses but are strong witnesses. As such the Carmicheal number, would be classified as prime when only testing for witnesses. But with strong witnesses, 561 would be seen to be composite. 

# ## Problem 4 
# 
# An integer N is a perfect power if $N = M^ e$ for some integers $M$ and $e > 1$. Construct a function that determines whether $N$ is a perfect power.

# 1. If $N = M^e$ for some M,e then $e \leq log_e N+1$.
# 2. For N and a fixed b, check if there exists an $M$ such that 
# $M^e=N.$

# In[400]:


def binarysearch(lista,l,r,x):
    if r>=l:
        median = l+(r-l) // 2
        if lista[median] == x:
            return x
        if lista[median] < x:
            return binarysearch(lista,l,median-1,x)
    
        if lista[median] > x:
            return binarysearch(lista,median+1,r,x)
    else:
        return -1
    
def isPerfectPower(N,e):
    base = [N]
    upperbound = len(bin(N)[2:])
    m = 2
    while m <= int(N**(1/float(e)))+1:
        for i in range(2,upperbound+1):
            if binarysearch(base,0,len(base)-1,m**i) == N:
                return True
        m=m+1
    return False
    
    
isPerfectPower(9,2)


def isPerfect(N):
    upperbound = len(bin(N)[2:])
    e = 2
    while e< upperbound:
        if isPerfectPower(N,e) == True:
            return True
        e= e+1
    return False

isPerfect(625)


# ## The Algorithm
# 
# With the previous results, we can now implement the Miller-Rabin test.
# 
# **The Miller-Rabin primality test**
# 
# Input: Integer $N$ and parameter $t$  
# Output: A decision as to whether $N$ is prime or composite  
# 
# 
# if $N$ is even, return false  
# if $N$ is a perfect power, return false  
# for $j = 1$ to $t$:  
# 
#         uniformly select an element a from {1,..., N - 1}  
#         if gcd(a,N)= 1 return false
#         if a is a strong witness return false
# 
# return true
# 
# 
# **Theorem**: If N is prime, then the Miller-Rabin test always out-
# puts "prime". If N is composite, then the algorithm outputs "prime" with
# probability at most $2^t$.

# ## Problem 5
# 
# Implement the Miller-Rabin primality test. Note that random.randint(a, b) randomly selects an integer from the range [a,b]. Note this function is not a true source of randomness. 

# In[401]:


import random
random.randint(1,10)


# In[635]:


def MRisPrime(N,t):
    if N%2 == 0:
        if N == 2:
            return True
        if N != 2:
            return False
    if isPerfect(N)==True:
        return False
    for i in range(0,t):
        x=random.randint(2,N-1)
        if RGCD(x,N)>1:
            #print('here1',x,RGCD(x,N))
            return False
        if isStrongWitness(x,N)==True:
            #print('here2',x)
            return False
        
    return True




# In[676]:


def firstnprimes(n,accuracy):
    '''
    firstnprimes: Finds first n primes
    Input: n - Upper Bound
           accuracy - the algorithm outputs "prime" with probability at most  2^𝑡 when x is a composite number 
    Output: returns list of primes
    
    '''
    count = []
    for i in range(2,n):
        if MRisPrime(i,accuracy):
            count.append(i) 
    return count


def firstnfound(n,accuracy):
    '''
    firstnfound: Find all primes less than n such using Miller-Rabin Primality Test.
    Input: n - Upper Bound
           accuracy - the algorithm outputs "prime" with probability at most  2^𝑡 when x is a composite number 
    Output: Number of primes below n 
    
    '''
    count = 0
    for i in range(2,n):
        if MRisPrime(i,accuracy):
            count = count +1 
    return count

def simulateFirstNFound(iterations,numberofprimes,n,accuracy):
    '''
    firstnfound: Simulates the firstnfound for a given number of iterations. Returns the probability that firstnfound
    found the correct number of primes 
    
    Input: iterations - Number of iterations the experiment is ran
            numberofprimes - Number of primes that is below n 
            n - Upper Bound
           accuracy - the algorithm outputs "prime" with probability at most  2^𝑡 when x is a composite number 
    Output: Probability of Success
    
    '''
    count = 0
    for i in range(0,iterations):
        if numberofprimes !=firstnfound(n,accuracy):
            count = count + 1 
    print(count,iterations)
    return count/iterations

#simulateFirstNFound(10,168,1000,5)

def SeiveofE(upper):   
    '''
    SieveofE: Finds First N primes 
    
    Input: upper - upper limit to check primes   
    Output: Returns list of primes
    
    '''
    ok=[x for x in range(2,upper)]
    bool1=[1 for x in range(2,upper)]
    
    count =0
    while count < len(bool1):
        if bool1[count] == True:
            N = ok[count]
            for i in ok:
                if N*i in ok:
                    bool1[N*i-2]=0
        count=count+1 
        
    primes=[]
    for i in range(0,len(bool1)):
        if bool1[i]==1:
            primes.append(ok[i])
    return primes




