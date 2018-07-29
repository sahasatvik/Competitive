#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randrange
from miller_rabin import is_prime_miller

def mrange(lo, hi):
    while lo < hi:
        yield lo
        lo += 1

for i in mrange(int(sys.argv[1]), int(sys.argv[2])):
    if is_prime_miller(i):
        print i
