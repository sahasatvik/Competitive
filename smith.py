#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Displays the Smith numbers within a given range.
# A number 'n' is a Smith number if the sum of its digits is equal
# to the sum of the sums of the digits of its prime factorization.
# For simplicity, prime numbers will be ignored.

# Usage : ./smith,py [upper limit [lower limit]]

import sys, factors

def sum_digits(n):
    return sum(map(int, str(n)))

lo = 1
hi = int(sys.argv[1])
if (len(sys.argv) > 2):
    lo = int(sys.argv[2])

for n in xrange(lo, hi):
    f = factors.factorize(n)
    sd = sum_digits(n)
    sp = sum(map(sum_digits, f))
    if len(f) > 1 and sd == sp:
        fm = '{:>' + str(len(str(hi))) + 'd} : {}'
        print fm.format(n, ', '.join(str(x) for x in f))
