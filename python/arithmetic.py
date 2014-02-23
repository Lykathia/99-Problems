#!/usr/bin/env python
# https://sites.google.com/site/prologsite/prolog-problems/2

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
    def prime_gen(n):
        for prime in [i for i in range(2,n) if is_prime(i)]:
            yield prime

    res = []
    primes = prime_gen(n)
    while(n > 1):
        prime = next(primes)
        while(n%prime == 0):
            res.append(prime)
            n/=prime
    return res

assert(prime_factors(315) == [3,3,5,7])
assert(prime_factors(4) == [2,2])
print("2.02 -- PASSED")
