#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

class ElevatorException(Exception):
    pass

class Elevator(object):
    DOOR_CLOSED = 'E'
    DOOR_OPENED = 'B'
    MOVE_TIME = 2 #階を移動するのに必要な時間
    OPEN_TIME = 5 #ドアが開いてから閉じるまでの時間

    def __init__(self, elevator_id, book):
        self.elevator_id = elevator_id
        self.floor = 1 #今の階
        self.time = 0  #前回の動作を行った時の時間
        self.door_state = self.DOOR_CLOSED #ドアの状態
        self.open_time = 0 #ドアが最後に開いた時間
        self.book = book

    def _open_door(self, time):
        self.door_state = self.DOOR_OPENED
        self.open_time = time

    def _close_door(self, time):
        if self.door_state==self.DOOR_CLOSED:
            return
        if time-self.open_time<self.OPEN_TIME:
            raise ElevatorException('The door cannot close')
        self.door_state = self.DOOR_CLOSED

    def _move(self, time, to):
        if self.door_state==self.DOOR_OPENED:
            raise ElevatorException('The door is opened, the elevator cannot move')
        if abs(to-self.floor)*self.MOVE_TIME > time-self.time:
            raise ElevatorException('Too Fast')
        self.floor = to

    def action(self, time, floor, action, book_ids):
        if self.floor != floor:
            self._move(time, floor)
        if action==self.DOOR_CLOSED:
            self._close_door(time)
            for book_id in book_ids:
                self.book[book_id].into_elevator(time)
        elif action==self.DOOR_OPENED:
            self._open_door(time)
            for book_id in book_ids:
                self.book[book_id].out_elevator(time)
        self.time = time

class BookItem(object):
    def __init__(self, book_id, book_time, floor_from, floor_to):
        self.book_id = book_id #入力データの識別番号
        self.book_time = book_time #予約時間
        self.floor_from = floor_from #乗る階
        self.floor_to = floor_to #降りる階
        self.in_time = -1 #実際に乗った時間
        self.out_time = -1 #実際に降りた時間

    def into_elevator(self, time):
        if self.in_time>=0:
            raise ElevatorException('')
        self.in_time = time

    def out_elevator(self, time):
        self.out_time = time

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    book = {}
    for line in open(input_file):
        item = [int(s) for s in line.split(',')]
        input_id, book_time, floor_from, floor_to = item
        book[input_id] = BookItem(input_id, book_time, floor_from, floor_to)

    elevators = {}
    for line in open(output_file):
        item = line.strip().split(',')
        elevator_id = int(item[0])
        time = int(item[1])
        floor = int(item[2])
        action = item[3]
        book_ids = [int(i) for i in item[4:] if i!='0']
        if elevator_id not in elevators:
            elevators[elevator_id] = Elevator(elevator_id, book)
        elevator = elevators[elevator_id]
        elevator.action(time, floor, action, book_ids)
    
    sum_waiting_time = 0
    flag = False
    for book in book.itervalues():
        if book.out_time<0:
            flag = True
        else:
            sum_waiting_time += book.out_time - book.book_time

    if flag:
        print 'すべての申告が満たされていません'
    print '合計待ち時間: %d' % sum_waiting_time
if __name__=='__main__':
    try:
        main()
    except ElevatorException, e:
        print e
