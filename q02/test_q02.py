#!/usr/bin/env python
# -*- coding:utf-8 -*-

from q02 import kaijo

class TestKaijo:
    delta = 1e-5

    def eq(self, a, b):
        print a, b, abs((a-b)/b)
        assert abs((a-b)/b)<self.delta

    def test1(self):
        self.eq(kaijo(0), 1)
        self.eq(kaijo(1), 1)
        self.eq(kaijo(2), 2)
        self.eq(kaijo(3), 6)
        self.eq(kaijo(4), 24)
        self.eq(kaijo(5), 120)
        self.eq(kaijo(6), 720)
        self.eq(kaijo(7), 5040)
        self.eq(kaijo(8), 40320)
        self.eq(kaijo(9), 362880)
        self.eq(kaijo(10), 3628800)

    def test2(self):
        self.eq(kaijo(0.5), 0.886226925)
        self.eq(kaijo(1.5), 1.32934039)
        self.eq(kaijo(2.5), 3.32335097)
        self.eq(kaijo(3.5), 11.6317284)
        self.eq(kaijo(4.5), 52.3427778)
        self.eq(kaijo(5.5), 287.885278)
        self.eq(kaijo(6.5), 1871.25431)
        self.eq(kaijo(7.5), 14034.4073)
        self.eq(kaijo(8.5), 119292.462)
        self.eq(kaijo(9.5), 1133278.39)

    def test3(self):
        self.eq(kaijo(-1.9), -10.5705641)
        self.eq(kaijo(-1.8), -5.73855464)
        self.eq(kaijo(-1.7), -4.27366998)
        self.eq(kaijo(-1.6), -3.69693257)
        self.eq(kaijo(-1.5), -3.5449077)
        self.eq(kaijo(-1.4), -3.72298062)
        self.eq(kaijo(-1.3), -4.32685111)
        self.eq(kaijo(-1.2), -5.82114857)
        self.eq(kaijo(-1.1), -10.686287)
