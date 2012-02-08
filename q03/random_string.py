#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import itertools

def random_chr():
    r = 16
    while True:
        r = (r * 1103515245 + 12345) & 0xFFFFFFFF
        yield chr(0x61 + ( 26 * ( r / 0x10000) ) / 0x10000)

def main():
    for c in itertools.islice(random_chr(), 0, 300000):
        sys.stdout.write(c)

if __name__=='__main__':
    main()
