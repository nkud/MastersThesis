#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

INPUT_DIR_WORD = 'result'

print '--> extraction has started'

ls = os.listdir('.')

out = open('cancercell-size-master.txt', 'w')
for l in ls:
    n = 0
    if not INPUT_DIR_WORD in l: continue
    cancerfilepass = '%s/bin/cancercell-size.txt' % l
    file = open(cancerfilepass, 'r')
    for line in file:
        n += 1
        line = line.split()
        out.write('%s,' % line[1])
        #if n > 300: break
    out.write('\n')

print '--> %d directories' % n
raw_input('--> done')