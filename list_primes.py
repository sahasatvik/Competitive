#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from miller_rabin import is_prime_miller

def mrange(lo, hi):
    while lo < hi:
        yield lo
        lo += 1

def list_primes(lo, hi):
    l = []
    for i in mrange(int(sys.argv[1]), int(sys.argv[2])):
        if is_prime_miller(i):
            l.append(i)
    return l

if __name__ == "__main__":
    for i in mrange(int(sys.argv[1]), int(sys.argv[2])):
        if is_prime_miller(i):
            print i
