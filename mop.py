#!/usr/bin/python

# Displays the shortest string of multiplication signs (x's), ones (1's)
# and plusses (+'s) that evaluates to the number passed to it.

# Usage : ./mop.py [number]

import sys

def mop_exp(n):
    if n < 1 :                          # invalid case
        return ''
    elif n in [1, 2, 3, 5] :            # base cases
        return ones(n)
    for i in [2, 3, 5] :                # for multiples of the base case, factor them out
        if (n % i) == 0 :
            return '(' + ones(i) + ') x (' + mop_exp(n / i) + ')'
    return '1 + ' + mop_exp(n - 1)      # recurse by pulling out a one (1)

def ones(n):                            # generate a string of ones (1's) with each other
    return '1' + (' + 1' * (n - 1))

def count_ones(s):                      # count the number of ones (1's) in a string
    return len(filter( lambda a: a == '1', s))

exp = mop_exp(int(sys.argv[1])          # call mop_exp on cli input
print "MOPExp : {}".format(exp)
print "Length : {}".format(count_ones(exp))
