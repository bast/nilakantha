#!/usr/bin/env python

import os
import sys


def get_term(n):
    return 4.0/(n*(n + 1)*(n + 2))


def get_terms(num_terms):
    l = []
    n = 2
    for i in range(num_terms):
        sign = (-1)**i
        l.append(sign*get_term(n))
        n += 2
    return l


def main():
    NUM_COMMITS = 500
    BAD_COMMIT = 137
    NUM_TERMS = 15
    BAD_TERM = 5

    if os.path.exists('.git'):
        sys.stderr.write('ERROR: do not run this script in an existing repo\n')
        sys.exit(1)
    os.system('git init')

    l = get_terms(NUM_TERMS)

    for i in range(NUM_COMMITS):
        with open('get_pi.py', 'w') as f:
            f.write('# commit {0}\n'.format(i + 1))
            for k, term in enumerate(l):
                t = l[k]
                if i >= BAD_COMMIT - 1 and k == BAD_TERM - 1:
                    t += 0.4321
                if k == 0:
                    f.write('t{0} = 3.0 + {1}'.format(k, t))
                elif k == len(l) - 1:
                    f.write('print(t{0})'.format(k - 1))
                else:
                    f.write('t{0} = t{1} + {2}'.format(k, k - 1, t))
                if k == i%NUM_TERMS:
                    f.write('  # this comment is added to obfuscate git blame\n')
                else:
                    f.write('\n')
        os.system('git add get_pi.py; git commit get_pi.py -m "commit number %i"' % (i+1))


if __name__ == '__main__':
    main()
