#!/usr/bin/python

import sys

def mopexp(n):
    if n < 1 :
        return ''
    elif n in [1, 2, 3, 5] :
        return ones(n)
    for i in [2, 3, 5] :
        if (n % i) == 0 :
            return '(' + ones(i) + ') x (' + mopexp(n / i) + ')'
    return '1 + ' + mopexp(n - 1)

def ones(n):
    return '1' + (' + 1' * (n - 1))

def mop(n):
    return len(filter( lambda a: a == '1', mopexp(n)))

n = int(sys.argv[1])
print "MOPExp : {}".format(mopexp(n))
print "Length : {}".format(mop(n))
