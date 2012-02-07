#!/usr/bin/env python

import datetime

class ClockOfLife:
    def __init__(self, year, month, day, life):
        self.birth_day = datetime.datetime(year, month, day)
        if month==2 and day==29:
            self.dead_day = datetime.datetime(year+life+1, month, day-1) + datetime.timedelta(1)
        else:
            self.dead_day = datetime.datetime(year+life+1, month, day)
        self.total_seconds = (self.dead_day - self.birth_day).total_seconds()

    def get_time(self, now):
        life_seconds = (now - self.birth_day).total_seconds()
        return datetime.timedelta(life_seconds/self.total_seconds)

def main():
    year = int(raw_input('Birth Year?:'))
    month = int(raw_input('Birth Month?:'))
    day = int(raw_input('Birth Day?:'))
    life = int(raw_input('How many years will you live?:'))
    clock = ClockOfLife(year, month, day, life)
    print str(clock.get_time(datetime.datetime.now()))

if __name__=="__main__":
    main()
