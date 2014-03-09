#!/usr/bin/env python
# https://sites.google.com/site/prologsite/prolog-problems/2

import itertools
import math

# 2.01 Prime Number
def is_prime(n):
    if (n%2) == 0 and n > 2:
        return False
    return all(n%i for i in range(3, int(math.sqrt(n)+1), 2))

assert(is_prime(3) == True)
assert(is_prime(6) == False)
print("2.01 -- PASSED")

# 2.02 Prime Factors
def prime_factors(n):
    def prime_gen(lower, upper):
        for prime in [i for i in range(lower, upper+1) if is_prime(i)]:
            yield prime

    res = []
    primes = prime_gen(2, n)
    while(n > 1):
        prime = next(primes)
        while(n%prime == 0):
            res.append(prime)
            n/=prime
    return res

assert(prime_factors(315) == [3,3,5,7])
assert(prime_factors(4) == [2,2])
print("2.02 -- PASSED")

# 2.03 Prime Factors'
def prime_factors_multi(n):
    l = prime_factors(n)
    return [[sublist[0], len(sublist)] for sublist in [list(g) for _, g in itertools.groupby(l)]]

assert(prime_factors_multi(315) == [[3,2],[5,1],[7,1]])
assert(prime_factors_multi(4) == [[2,2]])
print("2.03 -- PASSED")

# 2.04 Prime Generator -- Copy of helper function in 2.02
def prime_gen(lower, upper):
    for prime in [i for i in range(lower, upper+1) if is_prime(i)]:
        yield prime

assert(list(prime_gen(2,17)) == [2,3,5,7,11,13,17])
assert(list(prime_gen(4,17)) == [5,7,11,13,17])
print("2.04 -- PASSED")

# 2.05 Goldbach's conjecture
def goldbach(n):
    pass

assert(goldbach(28) == [5,23])
print("2.05 -- PASSED")
