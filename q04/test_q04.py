# -*- coding:utf-8 -*-

from q04 import *

class testNode:
    def test_fromstring(self):
        tests = [
            ('0:4:', 0, 0.25),
            ('1:4:', 1, 0.25),
            ('2:4:', 3, 0.25),
            ('3:4:', 5, 0.25),
            ('4:4:', 6, 0.25),
            ('5:4:', 8, 0.25),
            ('6:4:', 10, 0.25),

            ('1:4:s', 2, 0.25),
            ('1:4:x', 3, 0.25),
            ('2:4:b', 2, 0.25),
            ('2:4:d', 1, 0.25),

            ('0:1:', 0, 1.0),
            ('0:1.:', 0, 1.5),

            ('-10:4:', -18, 0.25),
            ('18:4:', 30, 0.25),
            (':4:', None, 0.25),
            ]
        for s, level, length in tests:
            print s
            n = Note.fromstring(s)
            assert n.level==level and n.length==length
