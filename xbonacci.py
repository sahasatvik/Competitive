#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Displays the first 'n' terms of a fibonacci-like sequence, where the
# number next term is the sum of the previous 'x' terms. The initial
# signature contains the first 'x' terms.

# Usage: ./xbonacci.py [number of terms] [term_1 [term_2 [term_3 [...]]]]

import sys

def xbonacci(signature, n):                 # wrapper for the xbonacci sequence
    return xb_seq(signature, len(signature), n - len(signature))
def xb_seq(elements, x, l):                 # returns a list of numbers in the sequence
    if l < 1:
        return elements                     # base case
    return xb_seq(elements + [sum(elements[-x:])], x, l - 1)

if __name__ == '__main__':
    n = int(sys.argv[1])                    # get cli arguments
    nums = map(int, sys.argv[2:])
    print xbonacci(nums, n)
