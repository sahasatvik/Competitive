#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randrange
from miller_rabin import is_prime_miller

def right_truncatable_primes(n):
    if not n == '':
        print n
    for d in '123456789':
        if is_prime_miller(int(n + d)):
            right_truncatable_primes(n + d)

if __name__ == '__main__':
    right_truncatable_primes(int(sys.argv[1]))
