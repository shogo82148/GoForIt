#!/usr/bin/env python

import sys

def main():
    time = 0
    floor = 1
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        item = [int(s) for s in line.split(',')]
        input_id, book_time, floor_from, floor_to = item
        time = max(book_time-5, time+2*abs(floor_from-floor))
        print '1,%d,%d,B,0,0,0,0,0' % (time, floor_from)
        time += 5
        print '1,%d,%d,E,%d,0,0,0,0' % (time, floor_from, input_id)
        time += 2*abs(floor_from-floor_to)
        print '1,%d,%d,B,%d,0,0,0,0' % (time, floor_to, input_id)
        time += 5
        print '1,%d,%d,E,0,0,0,0,0' % (time, floor_to)
        floor = floor_to
if __name__=='__main__':
    main()
