#!/usr/bin/env python

import os
import sys
from random import shuffle

BAD_COMMIT = 137

def get_term(n):
    return 4.0/(n*(n + 1)*(n + 2))

l = []
n = 2
for i in range(100):
    sign = (-1)**i
    l.append(sign*get_term(n))
    n += 2

if os.path.exists('.git'):
    sys.stderr.write('ERROR: do not run this script in an existing repo\n')
    sys.exit(1)

os.system('git init')

for i in range(1000):
    if i == BAD_COMMIT - 1:
       l[42] += 0.123
    shuffle(l)
    code = 'print(3.0 + sum(%s))' % l
    with open('get_pi.py', 'w') as f:
        f.write(code)
    os.system('git add get_pi.py; git commit get_pi.py -m "commit number %i"' % (i+1))
