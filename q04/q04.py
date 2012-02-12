#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import random

class Note(object):
    """ 一つの音符を表すクラス """

    _tone2level = [0, 1, 3, 5, 6, 8, 10]
    _level2tone = [(0, ''), (1, ''), (2, 'b'), (2, ''),
                   (3,'b'), (3, ''), (4,''), (5,'b'),
                   (5,''), (6,'b'), (6,''), (7,'b')]

    def __init__(self, level, length):
        self.level = level
        self.length = length

    def __str__(self):
        if not self.level is None:
            tone, accidental = self._level2tone[self.level%12]
            tone += self.level/12*7
            tone = str(tone)
        else:
            tone, accidental = '', ''

        l = int(self.length*32)
        if 32%l==0:
            length = str(32/l)
        else:
            length = str(48/l) + '.'
        return ':'.join( (tone, length, accidental) )

    @classmethod
    def fromstring(cls, note):
        tone, length, accidental = note.split(':')
        
        #十二律音階での音の高さを計算
        if tone!='':
            tone = int(tone)
            level = tone/7*12 + cls._tone2level[tone%7]
            if accidental=='s':
                level += 1
            elif accidental=='x':
                level += 2
            elif accidental=='b':
                level -= 1
            elif accidental=='d':
                level -= 2
        else:
            level = None

        #音の長さを計算
        l = 1.0
        if length[-1]=='.':
            l *= 1.5
            length = length[:-1]
        l /= int(length)

        return Note(level, l)

class Melody(list):
    def __str__(self):
        return ','.join(str(n) for n in self)

    @classmethod
    def fromstring(cls, melody):
        notes = (Note.fromstring(n) for n in melody.split(','))
        return Melody(notes)

    def feature(self):
        f = 0
        last_node = self[0]
        for n in self[1:]:
            diff = 0
            if not(n.level is None or last_node.level is None):
                diff = n.level - last_node.level
            f += abs(diff)+n.length/last_node.length - 1
            last_node = n
        return int(f+1e-5)

def compose(G):
    Gf = G.feature()
    m = Melody(Note.fromstring('-2:1:') for i in range(3))
    m[1].level += (Gf-m.feature())/2
    if Gf%2!=0:
        m[2].length *= 2
    return m
    
A = '-3:4:,-2:4:,-1:4:,0:4:b,-1:4:,-2:4:,-3:4:,:4:,-1:4:,0:4:b,1:4:,2:4:,1:4:,0:4:b,-1:4:,:4:'
B = '3:4:,2:4:,1:4:,0:4:b,1:4:,2:4:,3:4:,:4:,1:4:,0:4:b,-1:4:,-2:4:,-1:4:,0:4:b,1:4:,:4:'
C = '3:4:,2:4:,1:4:,0:4:,1:4:,2:4:,3:4:,:4:,1:8:,0:4.:,-1:4:,-2:4:,:8:,-1:4.:,0:8:,1:8:'
D = '-6:8:,-6:8:,-6:8:,-4:8:,-2:8:,-2:8:,-2:8:,:8:,-5:8:,-5:8:,-5:8:,-3:8:,-2:8:,-2:8:,' \
    '-2:8:,:8:,:8:,-2:8:,-2:8:,-1:8:b,-1:8:,-1:8:,-1:8:,-1:8:b,-2:4:,0:4:,1:4:,:4:'
E = '-6:8.:,-7:16:,-6:8:,-5:8:,-4:8:,-4:8:,-4:4:,-3:8.:,-4:16:,-5:8:,-6:8:,-5:4:,:4:,-3:8:,' \
    '-5:4:,-5:8:,-4:8:,-4:8:,-3:8:,-3:8:,-4:8:,-4:8:,-5:8:,-5:8:,-6:4:,:4:'
F = '-6:2:,-5:4:,-6:8:,-5:8:,-4:4:,-2:4:,-4:4:,:4:,-5:4:,-5:4:,-6:4:,-5:4:,-4:2.:,:4:'
G = '-2:8.:,-1:16:,-2:8.:,-1:16:,-2:4:,-4:4:,-4:8.:,-3:16:,-4:8.:,-3:16:,-4:4:,-6:4:,' \
    '-4:8:,:8:,-6:8.:,-5:16:,-4:8:,:8:,-6:8.:,-5:16:,-4:8.:,-4:16:,-2:8.:,-2:16:,-5:8.:,-4:16:,-5:4:'
def main():
    Af = Melody.fromstring(A).feature()
    Bf = Melody.fromstring(B).feature()
    Cf = Melody.fromstring(C).feature()
    Df = Melody.fromstring(D).feature()
    Ef = Melody.fromstring(E).feature()
    Ff = Melody.fromstring(F).feature()
    Gf = Melody.fromstring(G).feature()

    print 'i)'
    print 'A', Af
    print 'B', Bf
    print 'C', Cf
    assert abs(Af-Bf)>1e-5 and abs(Af-Cf)<1e-5

    print
    print 'ii)'
    print 'D', Df
    print 'E', Ef
    print 'F', Ff
    ans = 'No one'
    if abs(Df-Bf)<1e-5:
        ans = 'D'
    elif abs(Ef-Bf)<1e-5:
        ans = 'E'
    elif abs(Ff-Bf)<1e-5:
        ans = 'F'
    print '%s has same feature to B' % ans

    print
    print 'iii)'
    print 'G', Gf
    H = compose(Melody.fromstring(G))
    Hf = H.feature()
    print 'result:'
    print str(H)
    print 'Feature', Hf
    assert abs(Gf-Hf)<1e-5

if __name__=="__main__":
    main()
