#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from miller_rabin import is_prime_miller

n = int(sys.argv[1])
count = 0;
i, p = 2, 2

while count < n:
    if is_prime_miller(i, 20):
        p = i
        count += 1
    i += 1

print p
