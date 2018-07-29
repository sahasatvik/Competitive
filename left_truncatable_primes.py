#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randrange
from miller_rabin import is_prime_miller

def left_truncatable_primes(n):
    if not n == '':
        print n
    for d in '123456789':
        if is_prime_miller(int(d + n)):
            left_truncatable_primes(d + n)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        left_truncatable_primes(sys.argv[1])
    else:
        left_truncatable_primes('')
