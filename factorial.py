"""
Factorials: go-to "does the candidate know of recursion?" problem for HR departments.
They even asked me to implement one one time, making me conclude they didn't
probably check my CV.

Yet this answer by Roman Andronov
    https://www.quora.com/How-do-I-solve-x-40320-mathematically/answer/Roman-Andronov
talks of "industrial-strength" factorial calculators. Let's implement one, then!
"""
from functools import reduce
from operator import mul

def find_primes(up_to:int)->list:
    primes = [2]
    for i in range(1,up_to):
        for prime in primes:
            if ((i+1) % prime is 0): break
        else: primes.append(i+1)
    return primes

def occurance_counter(up_to:int,prime:int)->int:
    c = 0
    i = 1
    while prime**i<=up_to:
        c += up_to//prime**i
        i += 1
    return c

def factorial(n:int)->int:
    if(n is 0): return 1
    else:
        p_powers = [p**occurance_counter(n,p) for p in find_primes(n)]
        return reduce(mul, p_powers)
