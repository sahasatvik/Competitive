#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lists the prime factors of a given number

# Usage : ./factors.py [number]

import sys, math

def primes(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for (prime, isPrime) in enumerate(p):
        if isPrime:
            yield prime
            for multiple in xrange(prime * prime, n, prime):
                p[multiple] = False

def factorize(n):
    if n == 1:
        return []
    for prime in primes(n):
        qt, rm = divmod(n, prime)
        if not rm:
            return [prime] + factorize(qt)
    return [n]

if __name__ == '__main__':
    n = int(sys.argv[1])
    print factorize(n)
