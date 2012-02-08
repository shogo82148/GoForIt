#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

#C言語による最新アルゴリズム事典より

LOG_2PI = math.log(2*math.pi)
N = 8

#Bernoulli数
B0 = 1
B1 = -1.0 / 2.0
B2 =  1.0 / 6.0
B4 = -1.0 / 30.0
B6 =  1.0 / 42.0
B8 = -1.0 / 30.0
B10 = 5.0 / 66.0
B12 = -691.0 / 2730.0
B14 = 7.0 / 6.0
B16 = -3617.0 / 510.0

def loggamma(x):
    v = 1.0
    while x<N:
        v *= x
        x += 1.0
    w = 1 / (x*x)
    return ((((((((((B16/(16*15))) * w + (B14/(14*13))) * w
                   +(B12/(12*11))) * w + (B10/(10* 9))) * w
                   +(B8 /( 8* 7))) * w + (B6 /( 6* 5))) * w
                   +(B4 /( 4* 3))) * w + (B2 /( 2* 1))) / x
            + 0.5 * LOG_2PI - math.log(v) - x + (x-0.5) * math.log(x))

def gamma(x):
    if x<0:
        return math.pi / (math.sin(math.pi*x) * math.exp(loggamma(1-x)))
    return math.exp(loggamma(x))

def kaijo(x):
    #return math.gamma(x+1)
    return gamma(x+1)

def main():
    while True:
        x = float(raw_input())
        if x==0:
            break
        print kaijo(x)

if __name__=="__main__":
    main()
