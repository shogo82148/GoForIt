import datetime
import q01

class testClockOfLife:
    delta = datetime.timedelta(microseconds=1000)
    def testMax1(self):
        clock = q01.ClockOfLife(2000, 12, 31, 80)

        ans = clock.get_time(datetime.datetime(2000,12,31))
        expect = datetime.timedelta(0)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

        ans = clock.get_time(datetime.datetime(2081,12,31))
        expect = datetime.timedelta(1)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

    def testMax2(self):
        clock = q01.ClockOfLife(2000, 12, 31, 200)

        ans = clock.get_time(datetime.datetime(2000,12,31))
        expect = datetime.timedelta(0)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

        ans = clock.get_time(datetime.datetime(2201,12,31))
        expect = datetime.timedelta(1)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta


    def testMin1(self):
        clock = q01.ClockOfLife(1990, 1, 1, 80)

        ans = clock.get_time(datetime.datetime(1990,1,1))
        expect = datetime.timedelta(0)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

        ans = clock.get_time(datetime.datetime(2071,1,1))
        expect = datetime.timedelta(1)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

    def testMin2(self):
        clock = q01.ClockOfLife(1900, 1, 1, 200)

        ans = clock.get_time(datetime.datetime(1900,1,1))
        expect = datetime.timedelta(0)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

        ans = clock.get_time(datetime.datetime(2101,1,1))
        expect = datetime.timedelta(1)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

    def testMid(self):
        clock = q01.ClockOfLife(2001, 1, 1, 1)

        ans = clock.get_time(datetime.datetime(2002,1,1))
        expect = datetime.timedelta(hours=12)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta

    def testLeap(self):
        clock = q01.ClockOfLife(2000, 2, 29, 1)

        ans = clock.get_time(datetime.datetime(2001,2,28,12))
        expect = datetime.timedelta(hours=12)
        print str(ans), str(expect)
        assert abs(ans-expect)<self.delta
