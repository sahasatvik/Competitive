#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from list_primes import list_primes

lo, hi = int(sys.argv[1]), int(sys.argv[2])
print reduce(lambda x, y: x + y, list_primes(lo, hi))
