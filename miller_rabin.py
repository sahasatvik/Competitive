#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randrange

def is_prime_miller(n, k=10):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) > 2:
        lo, hi = int(sys.argv[1]), int(sys.argv[2])
        while lo < hi:
            if is_prime_miller(lo):
                print lo
            lo += 1
    else:
        print is_prime_miller(int(sys.argv[1]))
