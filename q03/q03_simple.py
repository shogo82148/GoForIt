#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def main():
    word = sys.argv[1]
    rword = word[::-1]
    R = raw_input()

    for skip in xrange(1,len(R)/(len(word)-1)):
        for i in xrange(len(R)-skip*(len(word)-1)):
            t = R[i:i+len(word)*skip:skip]
            if t==word or t==rword:
                print '%s,%s' % (skip, i+1)
                sys.stdout.flush()

if __name__=="__main__":
    main()
