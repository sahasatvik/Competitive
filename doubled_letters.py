#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Displays the words with doubled letters in the given sentence.

# Usage : ./doubled_letters.py [sentence]

import sys, re

for word in sys.argv[1].split():
    if re.search(r'(\w)(\1)', word):
        print re.match(r'\w+', word).group(0)

