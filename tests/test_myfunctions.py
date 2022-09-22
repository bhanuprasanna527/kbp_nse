from kbp_nse import time_interval
import datetime

def test_time_interval():
    assert time_interval.get_interval(19, 10) == [datetime.datetime(2019, 10, 1, 0, 0),
 datetime.datetime(2019, 10, 3, 0, 0),
 datetime.datetime(2019, 10, 4, 0, 0),
 datetime.datetime(2019, 10, 7, 0, 0),
 datetime.datetime(2019, 10, 9, 0, 0),
 datetime.datetime(2019, 10, 10, 0, 0),
 datetime.datetime(2019, 10, 11, 0, 0),
 datetime.datetime(2019, 10, 14, 0, 0),
 datetime.datetime(2019, 10, 15, 0, 0),
 datetime.datetime(2019, 10, 16, 0, 0),
 datetime.datetime(2019, 10, 17, 0, 0),
 datetime.datetime(2019, 10, 18, 0, 0),
 datetime.datetime(2019, 10, 21, 0, 0),
 datetime.datetime(2019, 10, 22, 0, 0),
 datetime.datetime(2019, 10, 23, 0, 0),
 datetime.datetime(2019, 10, 24, 0, 0),
 datetime.datetime(2019, 10, 25, 0, 0),
 datetime.datetime(2019, 10, 29, 0, 0),
 datetime.datetime(2019, 10, 30, 0, 0),
 datetime.datetime(2019, 10, 31, 0, 0),
 datetime.datetime(2019, 11, 1, 0, 0),
 datetime.datetime(2019, 11, 4, 0, 0),
 datetime.datetime(2019, 11, 5, 0, 0),
 datetime.datetime(2019, 11, 6, 0, 0),
 datetime.datetime(2019, 11, 7, 0, 0),
 datetime.datetime(2019, 11, 8, 0, 0),
 datetime.datetime(2019, 11, 11, 0, 0),
 datetime.datetime(2019, 11, 13, 0, 0),
 datetime.datetime(2019, 11, 14, 0, 0),
 datetime.datetime(2019, 11, 15, 0, 0),
 datetime.datetime(2019, 11, 18, 0, 0),
 datetime.datetime(2019, 11, 19, 0, 0),
 datetime.datetime(2019, 11, 20, 0, 0),
 datetime.datetime(2019, 11, 21, 0, 0),
 datetime.datetime(2019, 11, 22, 0, 0),
 datetime.datetime(2019, 11, 25, 0, 0),
 datetime.datetime(2019, 11, 26, 0, 0),
 datetime.datetime(2019, 11, 27, 0, 0),
 datetime.datetime(2019, 11, 28, 0, 0),
 datetime.datetime(2019, 11, 29, 0, 0),
 datetime.datetime(2019, 12, 2, 0, 0),
 datetime.datetime(2019, 12, 3, 0, 0),
 datetime.datetime(2019, 12, 4, 0, 0),
 datetime.datetime(2019, 12, 5, 0, 0),
 datetime.datetime(2019, 12, 6, 0, 0),
 datetime.datetime(2019, 12, 9, 0, 0),
 datetime.datetime(2019, 12, 10, 0, 0),
 datetime.datetime(2019, 12, 11, 0, 0),
 datetime.datetime(2019, 12, 12, 0, 0),
 datetime.datetime(2019, 12, 13, 0, 0),
 datetime.datetime(2019, 12, 16, 0, 0),
 datetime.datetime(2019, 12, 17, 0, 0),
 datetime.datetime(2019, 12, 18, 0, 0),
 datetime.datetime(2019, 12, 19, 0, 0),
 datetime.datetime(2019, 12, 20, 0, 0),
 datetime.datetime(2020, 1, 1, 0, 0),
 datetime.datetime(2020, 1, 2, 0, 0),
 datetime.datetime(2020, 1, 3, 0, 0),
 datetime.datetime(2020, 1, 6, 0, 0),
 datetime.datetime(2020, 1, 7, 0, 0),
 datetime.datetime(2020, 1, 8, 0, 0),
 datetime.datetime(2020, 1, 9, 0, 0),
 datetime.datetime(2020, 1, 10, 0, 0),
 datetime.datetime(2020, 1, 13, 0, 0),
 datetime.datetime(2020, 1, 14, 0, 0),
 datetime.datetime(2020, 1, 15, 0, 0),
 datetime.datetime(2020, 1, 16, 0, 0),
 datetime.datetime(2020, 1, 17, 0, 0),
 datetime.datetime(2020, 1, 20, 0, 0),
 datetime.datetime(2020, 1, 21, 0, 0),
 datetime.datetime(2020, 1, 22, 0, 0),
 datetime.datetime(2020, 1, 23, 0, 0),
 datetime.datetime(2020, 1, 24, 0, 0),
 datetime.datetime(2020, 1, 27, 0, 0),
 datetime.datetime(2020, 1, 28, 0, 0),
 datetime.datetime(2020, 1, 29, 0, 0),
 datetime.datetime(2020, 1, 30, 0, 0),
 datetime.datetime(2020, 1, 31, 0, 0),
 datetime.datetime(2020, 2, 3, 0, 0),
 datetime.datetime(2020, 2, 4, 0, 0),
 datetime.datetime(2020, 2, 5, 0, 0),
 datetime.datetime(2020, 2, 6, 0, 0),
 datetime.datetime(2020, 2, 7, 0, 0),
 datetime.datetime(2020, 2, 10, 0, 0),
 datetime.datetime(2020, 2, 11, 0, 0),
 datetime.datetime(2020, 2, 12, 0, 0),
 datetime.datetime(2020, 2, 13, 0, 0),
 datetime.datetime(2020, 2, 14, 0, 0),
 datetime.datetime(2020, 2, 17, 0, 0),
 datetime.datetime(2020, 2, 18, 0, 0),
 datetime.datetime(2020, 2, 19, 0, 0),
 datetime.datetime(2020, 2, 20, 0, 0),
 datetime.datetime(2020, 2, 24, 0, 0),
 datetime.datetime(2020, 2, 25, 0, 0),
 datetime.datetime(2020, 2, 26, 0, 0),
 datetime.datetime(2020, 2, 27, 0, 0),
 datetime.datetime(2020, 2, 28, 0, 0),
 datetime.datetime(2020, 3, 2, 0, 0),
 datetime.datetime(2020, 3, 3, 0, 0),
 datetime.datetime(2020, 3, 4, 0, 0),
 datetime.datetime(2020, 3, 5, 0, 0),
 datetime.datetime(2020, 3, 6, 0, 0),
 datetime.datetime(2020, 3, 9, 0, 0),
 datetime.datetime(2020, 3, 11, 0, 0),
 datetime.datetime(2020, 3, 12, 0, 0),
 datetime.datetime(2020, 3, 13, 0, 0),
 datetime.datetime(2020, 3, 16, 0, 0),
 datetime.datetime(2020, 3, 17, 0, 0),
 datetime.datetime(2020, 3, 18, 0, 0),
 datetime.datetime(2020, 3, 19, 0, 0),
 datetime.datetime(2020, 3, 20, 0, 0),
 datetime.datetime(2020, 3, 23, 0, 0),
 datetime.datetime(2020, 3, 24, 0, 0),
 datetime.datetime(2020, 3, 25, 0, 0),
 datetime.datetime(2020, 3, 26, 0, 0),
 datetime.datetime(2020, 3, 27, 0, 0),
 datetime.datetime(2020, 3, 30, 0, 0),
 datetime.datetime(2020, 3, 31, 0, 0),
 datetime.datetime(2020, 4, 1, 0, 0),
 datetime.datetime(2020, 4, 3, 0, 0),
 datetime.datetime(2020, 4, 7, 0, 0),
 datetime.datetime(2020, 4, 8, 0, 0),
 datetime.datetime(2020, 4, 9, 0, 0),
 datetime.datetime(2020, 4, 13, 0, 0),
 datetime.datetime(2020, 4, 15, 0, 0),
 datetime.datetime(2020, 4, 16, 0, 0),
 datetime.datetime(2020, 4, 17, 0, 0),
 datetime.datetime(2020, 4, 20, 0, 0),
 datetime.datetime(2020, 4, 21, 0, 0),
 datetime.datetime(2020, 4, 22, 0, 0),
 datetime.datetime(2020, 4, 23, 0, 0),
 datetime.datetime(2020, 4, 24, 0, 0),
 datetime.datetime(2020, 4, 27, 0, 0),
 datetime.datetime(2020, 4, 28, 0, 0),
 datetime.datetime(2020, 4, 29, 0, 0),
 datetime.datetime(2020, 4, 30, 0, 0),
 datetime.datetime(2020, 5, 4, 0, 0),
 datetime.datetime(2020, 5, 5, 0, 0),
 datetime.datetime(2020, 5, 6, 0, 0),
 datetime.datetime(2020, 5, 7, 0, 0),
 datetime.datetime(2020, 5, 8, 0, 0),
 datetime.datetime(2020, 5, 11, 0, 0),
 datetime.datetime(2020, 5, 12, 0, 0),
 datetime.datetime(2020, 5, 13, 0, 0),
 datetime.datetime(2020, 5, 14, 0, 0),
 datetime.datetime(2020, 5, 15, 0, 0),
 datetime.datetime(2020, 5, 18, 0, 0),
 datetime.datetime(2020, 5, 19, 0, 0),
 datetime.datetime(2020, 5, 20, 0, 0),
 datetime.datetime(2020, 5, 21, 0, 0),
 datetime.datetime(2020, 5, 22, 0, 0),
 datetime.datetime(2020, 5, 26, 0, 0),
 datetime.datetime(2020, 5, 27, 0, 0),
 datetime.datetime(2020, 5, 28, 0, 0),
 datetime.datetime(2020, 5, 29, 0, 0),
 datetime.datetime(2020, 6, 1, 0, 0),
 datetime.datetime(2020, 6, 2, 0, 0),
 datetime.datetime(2020, 6, 3, 0, 0),
 datetime.datetime(2020, 6, 4, 0, 0),
 datetime.datetime(2020, 6, 5, 0, 0),
 datetime.datetime(2020, 6, 8, 0, 0),
 datetime.datetime(2020, 6, 9, 0, 0),
 datetime.datetime(2020, 6, 10, 0, 0),
 datetime.datetime(2020, 6, 11, 0, 0),
 datetime.datetime(2020, 6, 12, 0, 0),
 datetime.datetime(2020, 6, 15, 0, 0),
 datetime.datetime(2020, 6, 16, 0, 0),
 datetime.datetime(2020, 6, 17, 0, 0),
 datetime.datetime(2020, 6, 18, 0, 0),
 datetime.datetime(2020, 6, 19, 0, 0),
 datetime.datetime(2020, 6, 22, 0, 0),
 datetime.datetime(2020, 6, 23, 0, 0),
 datetime.datetime(2020, 6, 24, 0, 0),
 datetime.datetime(2020, 6, 25, 0, 0),
 datetime.datetime(2020, 6, 26, 0, 0),
 datetime.datetime(2020, 6, 29, 0, 0),
 datetime.datetime(2020, 6, 30, 0, 0),
 datetime.datetime(2020, 7, 1, 0, 0),
 datetime.datetime(2020, 7, 2, 0, 0),
 datetime.datetime(2020, 7, 3, 0, 0),
 datetime.datetime(2020, 7, 6, 0, 0),
 datetime.datetime(2020, 7, 7, 0, 0),
 datetime.datetime(2020, 7, 8, 0, 0),
 datetime.datetime(2020, 7, 9, 0, 0),
 datetime.datetime(2020, 7, 10, 0, 0),
 datetime.datetime(2020, 7, 13, 0, 0),
 datetime.datetime(2020, 7, 14, 0, 0),
 datetime.datetime(2020, 7, 15, 0, 0),
 datetime.datetime(2020, 7, 16, 0, 0),
 datetime.datetime(2020, 7, 17, 0, 0),
 datetime.datetime(2020, 7, 20, 0, 0),
 datetime.datetime(2020, 7, 21, 0, 0),
 datetime.datetime(2020, 7, 22, 0, 0),
 datetime.datetime(2020, 7, 23, 0, 0),
 datetime.datetime(2020, 7, 24, 0, 0),
 datetime.datetime(2020, 7, 27, 0, 0),
 datetime.datetime(2020, 7, 28, 0, 0),
 datetime.datetime(2020, 7, 29, 0, 0),
 datetime.datetime(2020, 7, 30, 0, 0),
 datetime.datetime(2020, 7, 31, 0, 0),
 datetime.datetime(2020, 8, 3, 0, 0),
 datetime.datetime(2020, 8, 4, 0, 0),
 datetime.datetime(2020, 8, 5, 0, 0),
 datetime.datetime(2020, 8, 6, 0, 0),
 datetime.datetime(2020, 8, 7, 0, 0),
 datetime.datetime(2020, 8, 10, 0, 0),
 datetime.datetime(2020, 8, 11, 0, 0),
 datetime.datetime(2020, 8, 12, 0, 0),
 datetime.datetime(2020, 8, 13, 0, 0),
 datetime.datetime(2020, 8, 14, 0, 0),
 datetime.datetime(2020, 8, 17, 0, 0),
 datetime.datetime(2020, 8, 18, 0, 0),
 datetime.datetime(2020, 8, 19, 0, 0),
 datetime.datetime(2020, 8, 20, 0, 0),
 datetime.datetime(2020, 8, 21, 0, 0),
 datetime.datetime(2020, 8, 24, 0, 0),
 datetime.datetime(2020, 8, 25, 0, 0),
 datetime.datetime(2020, 8, 26, 0, 0),
 datetime.datetime(2020, 8, 27, 0, 0),
 datetime.datetime(2020, 8, 28, 0, 0),
 datetime.datetime(2020, 8, 31, 0, 0),
 datetime.datetime(2020, 9, 1, 0, 0),
 datetime.datetime(2020, 9, 2, 0, 0),
 datetime.datetime(2020, 9, 3, 0, 0),
 datetime.datetime(2020, 9, 4, 0, 0),
 datetime.datetime(2020, 9, 7, 0, 0),
 datetime.datetime(2020, 9, 8, 0, 0),
 datetime.datetime(2020, 9, 9, 0, 0),
 datetime.datetime(2020, 9, 10, 0, 0),
 datetime.datetime(2020, 9, 11, 0, 0),
 datetime.datetime(2020, 9, 14, 0, 0),
 datetime.datetime(2020, 9, 15, 0, 0),
 datetime.datetime(2020, 9, 16, 0, 0),
 datetime.datetime(2020, 9, 17, 0, 0),
 datetime.datetime(2020, 9, 18, 0, 0),
 datetime.datetime(2020, 9, 21, 0, 0),
 datetime.datetime(2020, 9, 22, 0, 0),
 datetime.datetime(2020, 9, 23, 0, 0),
 datetime.datetime(2020, 9, 24, 0, 0),
 datetime.datetime(2020, 9, 25, 0, 0),
 datetime.datetime(2020, 9, 28, 0, 0),
 datetime.datetime(2020, 9, 29, 0, 0),
 datetime.datetime(2020, 9, 30, 0, 0),
 datetime.datetime(2020, 10, 1, 0, 0),
 datetime.datetime(2020, 10, 5, 0, 0),
 datetime.datetime(2020, 10, 6, 0, 0),
 datetime.datetime(2020, 10, 7, 0, 0),
 datetime.datetime(2020, 10, 8, 0, 0),
 datetime.datetime(2020, 10, 9, 0, 0),
 datetime.datetime(2020, 10, 12, 0, 0),
 datetime.datetime(2020, 10, 13, 0, 0),
 datetime.datetime(2020, 10, 14, 0, 0),
 datetime.datetime(2020, 10, 15, 0, 0),
 datetime.datetime(2020, 10, 16, 0, 0),
 datetime.datetime(2020, 10, 19, 0, 0),
 datetime.datetime(2020, 10, 20, 0, 0),
 datetime.datetime(2020, 10, 21, 0, 0),
 datetime.datetime(2020, 10, 22, 0, 0),
 datetime.datetime(2020, 10, 23, 0, 0),
 datetime.datetime(2020, 10, 26, 0, 0),
 datetime.datetime(2020, 10, 27, 0, 0),
 datetime.datetime(2020, 10, 28, 0, 0),
 datetime.datetime(2020, 10, 29, 0, 0),
 datetime.datetime(2020, 10, 30, 0, 0),
 datetime.datetime(2020, 11, 2, 0, 0),
 datetime.datetime(2020, 11, 3, 0, 0),
 datetime.datetime(2020, 11, 4, 0, 0),
 datetime.datetime(2020, 11, 5, 0, 0),
 datetime.datetime(2020, 11, 6, 0, 0),
 datetime.datetime(2020, 11, 9, 0, 0),
 datetime.datetime(2020, 11, 10, 0, 0),
 datetime.datetime(2020, 11, 11, 0, 0),
 datetime.datetime(2020, 11, 12, 0, 0),
 datetime.datetime(2020, 11, 13, 0, 0),
 datetime.datetime(2020, 11, 17, 0, 0),
 datetime.datetime(2020, 11, 18, 0, 0),
 datetime.datetime(2020, 11, 19, 0, 0),
 datetime.datetime(2020, 11, 20, 0, 0),
 datetime.datetime(2020, 11, 23, 0, 0),
 datetime.datetime(2020, 11, 24, 0, 0),
 datetime.datetime(2020, 11, 26, 0, 0),
 datetime.datetime(2020, 11, 27, 0, 0),
 datetime.datetime(2020, 12, 1, 0, 0),
 datetime.datetime(2020, 12, 2, 0, 0),
 datetime.datetime(2020, 12, 3, 0, 0),
 datetime.datetime(2020, 12, 4, 0, 0),
 datetime.datetime(2020, 12, 7, 0, 0),
 datetime.datetime(2020, 12, 8, 0, 0),
 datetime.datetime(2020, 12, 9, 0, 0),
 datetime.datetime(2020, 12, 10, 0, 0),
 datetime.datetime(2020, 12, 11, 0, 0),
 datetime.datetime(2020, 12, 14, 0, 0),
 datetime.datetime(2020, 12, 15, 0, 0),
 datetime.datetime(2020, 12, 16, 0, 0),
 datetime.datetime(2020, 12, 17, 0, 0),
 datetime.datetime(2020, 12, 18, 0, 0),
 datetime.datetime(2020, 12, 21, 0, 0),
 datetime.datetime(2021, 1, 1, 0, 0),
 datetime.datetime(2021, 1, 4, 0, 0),
 datetime.datetime(2021, 1, 5, 0, 0),
 datetime.datetime(2021, 1, 6, 0, 0),
 datetime.datetime(2021, 1, 7, 0, 0),
 datetime.datetime(2021, 1, 8, 0, 0),
 datetime.datetime(2021, 1, 11, 0, 0),
 datetime.datetime(2021, 1, 12, 0, 0),
 datetime.datetime(2021, 1, 13, 0, 0),
 datetime.datetime(2021, 1, 14, 0, 0),
 datetime.datetime(2021, 1, 15, 0, 0),
 datetime.datetime(2021, 1, 18, 0, 0),
 datetime.datetime(2021, 1, 19, 0, 0),
 datetime.datetime(2021, 1, 20, 0, 0),
 datetime.datetime(2021, 1, 21, 0, 0),
 datetime.datetime(2021, 1, 22, 0, 0),
 datetime.datetime(2021, 1, 25, 0, 0),
 datetime.datetime(2021, 1, 27, 0, 0),
 datetime.datetime(2021, 1, 28, 0, 0),
 datetime.datetime(2021, 1, 29, 0, 0),
 datetime.datetime(2021, 2, 1, 0, 0),
 datetime.datetime(2021, 2, 2, 0, 0),
 datetime.datetime(2021, 2, 3, 0, 0),
 datetime.datetime(2021, 2, 4, 0, 0),
 datetime.datetime(2021, 2, 5, 0, 0),
 datetime.datetime(2021, 2, 8, 0, 0),
 datetime.datetime(2021, 2, 9, 0, 0),
 datetime.datetime(2021, 2, 10, 0, 0),
 datetime.datetime(2021, 2, 11, 0, 0),
 datetime.datetime(2021, 2, 12, 0, 0),
 datetime.datetime(2021, 2, 15, 0, 0),
 datetime.datetime(2021, 2, 16, 0, 0),
 datetime.datetime(2021, 2, 17, 0, 0),
 datetime.datetime(2021, 2, 18, 0, 0),
 datetime.datetime(2021, 2, 19, 0, 0),
 datetime.datetime(2021, 2, 22, 0, 0),
 datetime.datetime(2021, 2, 23, 0, 0),
 datetime.datetime(2021, 2, 24, 0, 0),
 datetime.datetime(2021, 2, 25, 0, 0),
 datetime.datetime(2021, 2, 26, 0, 0),
 datetime.datetime(2021, 3, 1, 0, 0),
 datetime.datetime(2021, 3, 2, 0, 0),
 datetime.datetime(2021, 3, 3, 0, 0),
 datetime.datetime(2021, 3, 4, 0, 0),
 datetime.datetime(2021, 3, 5, 0, 0),
 datetime.datetime(2021, 3, 8, 0, 0),
 datetime.datetime(2021, 3, 9, 0, 0),
 datetime.datetime(2021, 3, 10, 0, 0),
 datetime.datetime(2021, 3, 12, 0, 0),
 datetime.datetime(2021, 3, 15, 0, 0),
 datetime.datetime(2021, 3, 16, 0, 0),
 datetime.datetime(2021, 3, 17, 0, 0),
 datetime.datetime(2021, 3, 18, 0, 0),
 datetime.datetime(2021, 3, 19, 0, 0),
 datetime.datetime(2021, 3, 22, 0, 0),
 datetime.datetime(2021, 3, 23, 0, 0),
 datetime.datetime(2021, 3, 24, 0, 0),
 datetime.datetime(2021, 3, 25, 0, 0),
 datetime.datetime(2021, 3, 26, 0, 0),
 datetime.datetime(2021, 3, 30, 0, 0),
 datetime.datetime(2021, 3, 31, 0, 0),
 datetime.datetime(2021, 4, 1, 0, 0),
 datetime.datetime(2021, 4, 5, 0, 0),
 datetime.datetime(2021, 4, 6, 0, 0),
 datetime.datetime(2021, 4, 7, 0, 0),
 datetime.datetime(2021, 4, 8, 0, 0),
 datetime.datetime(2021, 4, 9, 0, 0),
 datetime.datetime(2021, 4, 12, 0, 0),
 datetime.datetime(2021, 4, 13, 0, 0),
 datetime.datetime(2021, 4, 15, 0, 0),
 datetime.datetime(2021, 4, 16, 0, 0),
 datetime.datetime(2021, 4, 19, 0, 0),
 datetime.datetime(2021, 4, 20, 0, 0),
 datetime.datetime(2021, 4, 22, 0, 0),
 datetime.datetime(2021, 4, 23, 0, 0),
 datetime.datetime(2021, 4, 26, 0, 0),
 datetime.datetime(2021, 4, 27, 0, 0),
 datetime.datetime(2021, 4, 28, 0, 0),
 datetime.datetime(2021, 4, 29, 0, 0),
 datetime.datetime(2021, 4, 30, 0, 0),
 datetime.datetime(2021, 5, 3, 0, 0),
 datetime.datetime(2021, 5, 4, 0, 0),
 datetime.datetime(2021, 5, 5, 0, 0),
 datetime.datetime(2021, 5, 6, 0, 0),
 datetime.datetime(2021, 5, 7, 0, 0),
 datetime.datetime(2021, 5, 10, 0, 0),
 datetime.datetime(2021, 5, 11, 0, 0),
 datetime.datetime(2021, 5, 12, 0, 0),
 datetime.datetime(2021, 5, 14, 0, 0),
 datetime.datetime(2021, 5, 17, 0, 0),
 datetime.datetime(2021, 5, 18, 0, 0),
 datetime.datetime(2021, 5, 19, 0, 0),
 datetime.datetime(2021, 5, 20, 0, 0),
 datetime.datetime(2021, 5, 21, 0, 0),
 datetime.datetime(2021, 5, 24, 0, 0),
 datetime.datetime(2021, 5, 25, 0, 0),
 datetime.datetime(2021, 5, 26, 0, 0),
 datetime.datetime(2021, 5, 27, 0, 0),
 datetime.datetime(2021, 5, 28, 0, 0),
 datetime.datetime(2021, 5, 31, 0, 0),
 datetime.datetime(2021, 6, 1, 0, 0),
 datetime.datetime(2021, 6, 2, 0, 0),
 datetime.datetime(2021, 6, 3, 0, 0),
 datetime.datetime(2021, 6, 4, 0, 0),
 datetime.datetime(2021, 6, 7, 0, 0),
 datetime.datetime(2021, 6, 8, 0, 0),
 datetime.datetime(2021, 6, 9, 0, 0),
 datetime.datetime(2021, 6, 10, 0, 0),
 datetime.datetime(2021, 6, 11, 0, 0),
 datetime.datetime(2021, 6, 14, 0, 0),
 datetime.datetime(2021, 6, 15, 0, 0),
 datetime.datetime(2021, 6, 16, 0, 0),
 datetime.datetime(2021, 6, 17, 0, 0),
 datetime.datetime(2021, 6, 18, 0, 0),
 datetime.datetime(2021, 6, 21, 0, 0),
 datetime.datetime(2021, 6, 22, 0, 0),
 datetime.datetime(2021, 6, 23, 0, 0),
 datetime.datetime(2021, 6, 24, 0, 0),
 datetime.datetime(2021, 6, 25, 0, 0),
 datetime.datetime(2021, 6, 28, 0, 0),
 datetime.datetime(2021, 6, 29, 0, 0),
 datetime.datetime(2021, 6, 30, 0, 0),
 datetime.datetime(2021, 7, 1, 0, 0),
 datetime.datetime(2021, 7, 2, 0, 0),
 datetime.datetime(2021, 7, 5, 0, 0),
 datetime.datetime(2021, 7, 6, 0, 0),
 datetime.datetime(2021, 7, 7, 0, 0),
 datetime.datetime(2021, 7, 8, 0, 0),
 datetime.datetime(2021, 7, 9, 0, 0),
 datetime.datetime(2021, 7, 12, 0, 0),
 datetime.datetime(2021, 7, 13, 0, 0),
 datetime.datetime(2021, 7, 14, 0, 0),
 datetime.datetime(2021, 7, 15, 0, 0),
 datetime.datetime(2021, 7, 16, 0, 0),
 datetime.datetime(2021, 7, 19, 0, 0),
 datetime.datetime(2021, 7, 20, 0, 0),
 datetime.datetime(2021, 7, 22, 0, 0),
 datetime.datetime(2021, 7, 23, 0, 0),
 datetime.datetime(2021, 7, 26, 0, 0),
 datetime.datetime(2021, 7, 27, 0, 0),
 datetime.datetime(2021, 7, 28, 0, 0),
 datetime.datetime(2021, 7, 29, 0, 0),
 datetime.datetime(2021, 7, 30, 0, 0),
 datetime.datetime(2021, 8, 2, 0, 0),
 datetime.datetime(2021, 8, 3, 0, 0),
 datetime.datetime(2021, 8, 4, 0, 0),
 datetime.datetime(2021, 8, 5, 0, 0),
 datetime.datetime(2021, 8, 6, 0, 0),
 datetime.datetime(2021, 8, 9, 0, 0),
 datetime.datetime(2021, 8, 10, 0, 0),
 datetime.datetime(2021, 8, 11, 0, 0),
 datetime.datetime(2021, 8, 12, 0, 0),
 datetime.datetime(2021, 8, 13, 0, 0),
 datetime.datetime(2021, 8, 16, 0, 0),
 datetime.datetime(2021, 8, 17, 0, 0),
 datetime.datetime(2021, 8, 18, 0, 0),
 datetime.datetime(2021, 8, 20, 0, 0),
 datetime.datetime(2021, 8, 23, 0, 0),
 datetime.datetime(2021, 8, 24, 0, 0),
 datetime.datetime(2021, 8, 25, 0, 0),
 datetime.datetime(2021, 8, 26, 0, 0),
 datetime.datetime(2021, 8, 27, 0, 0),
 datetime.datetime(2021, 8, 30, 0, 0),
 datetime.datetime(2021, 8, 31, 0, 0),
 datetime.datetime(2021, 9, 1, 0, 0),
 datetime.datetime(2021, 9, 2, 0, 0),
 datetime.datetime(2021, 9, 3, 0, 0),
 datetime.datetime(2021, 9, 6, 0, 0),
 datetime.datetime(2021, 9, 7, 0, 0),
 datetime.datetime(2021, 9, 8, 0, 0),
 datetime.datetime(2021, 9, 9, 0, 0),
 datetime.datetime(2021, 9, 13, 0, 0),
 datetime.datetime(2021, 9, 14, 0, 0),
 datetime.datetime(2021, 9, 15, 0, 0),
 datetime.datetime(2021, 9, 16, 0, 0),
 datetime.datetime(2021, 9, 17, 0, 0),
 datetime.datetime(2021, 9, 20, 0, 0),
 datetime.datetime(2021, 9, 21, 0, 0),
 datetime.datetime(2021, 9, 22, 0, 0),
 datetime.datetime(2021, 9, 23, 0, 0),
 datetime.datetime(2021, 9, 24, 0, 0),
 datetime.datetime(2021, 9, 27, 0, 0),
 datetime.datetime(2021, 9, 28, 0, 0),
 datetime.datetime(2021, 9, 29, 0, 0),
 datetime.datetime(2021, 9, 30, 0, 0),
 datetime.datetime(2021, 10, 1, 0, 0),
 datetime.datetime(2021, 10, 4, 0, 0),
 datetime.datetime(2021, 10, 5, 0, 0),
 datetime.datetime(2021, 10, 6, 0, 0),
 datetime.datetime(2021, 10, 7, 0, 0),
 datetime.datetime(2021, 10, 8, 0, 0),
 datetime.datetime(2021, 10, 11, 0, 0),
 datetime.datetime(2021, 10, 12, 0, 0),
 datetime.datetime(2021, 10, 13, 0, 0),
 datetime.datetime(2021, 10, 14, 0, 0),
 datetime.datetime(2021, 10, 18, 0, 0),
 datetime.datetime(2021, 10, 19, 0, 0),
 datetime.datetime(2021, 10, 20, 0, 0),
 datetime.datetime(2021, 10, 21, 0, 0),
 datetime.datetime(2021, 10, 22, 0, 0),
 datetime.datetime(2021, 10, 25, 0, 0),
 datetime.datetime(2021, 10, 26, 0, 0),
 datetime.datetime(2021, 10, 27, 0, 0),
 datetime.datetime(2021, 10, 28, 0, 0),
 datetime.datetime(2021, 10, 29, 0, 0),
 datetime.datetime(2021, 11, 1, 0, 0),
 datetime.datetime(2021, 11, 2, 0, 0),
 datetime.datetime(2021, 11, 3, 0, 0),
 datetime.datetime(2021, 11, 8, 0, 0),
 datetime.datetime(2021, 11, 9, 0, 0),
 datetime.datetime(2021, 11, 10, 0, 0),
 datetime.datetime(2021, 11, 11, 0, 0),
 datetime.datetime(2021, 11, 12, 0, 0),
 datetime.datetime(2021, 11, 15, 0, 0),
 datetime.datetime(2021, 11, 16, 0, 0),
 datetime.datetime(2021, 11, 17, 0, 0),
 datetime.datetime(2021, 11, 18, 0, 0),
 datetime.datetime(2021, 11, 22, 0, 0),
 datetime.datetime(2021, 11, 23, 0, 0),
 datetime.datetime(2021, 11, 24, 0, 0),
 datetime.datetime(2021, 11, 25, 0, 0),
 datetime.datetime(2021, 11, 26, 0, 0),
 datetime.datetime(2021, 11, 29, 0, 0),
 datetime.datetime(2021, 11, 30, 0, 0),
 datetime.datetime(2021, 12, 1, 0, 0),
 datetime.datetime(2021, 12, 2, 0, 0),
 datetime.datetime(2021, 12, 3, 0, 0),
 datetime.datetime(2021, 12, 6, 0, 0),
 datetime.datetime(2021, 12, 7, 0, 0),
 datetime.datetime(2021, 12, 8, 0, 0),
 datetime.datetime(2021, 12, 9, 0, 0),
 datetime.datetime(2021, 12, 10, 0, 0),
 datetime.datetime(2021, 12, 13, 0, 0),
 datetime.datetime(2021, 12, 14, 0, 0),
 datetime.datetime(2021, 12, 15, 0, 0),
 datetime.datetime(2021, 12, 16, 0, 0),
 datetime.datetime(2021, 12, 17, 0, 0),
 datetime.datetime(2021, 12, 20, 0, 0),
 datetime.datetime(2021, 12, 21, 0, 0),
 datetime.datetime(2022, 1, 3, 0, 0),
 datetime.datetime(2022, 1, 4, 0, 0),
 datetime.datetime(2022, 1, 5, 0, 0),
 datetime.datetime(2022, 1, 6, 0, 0),
 datetime.datetime(2022, 1, 7, 0, 0),
 datetime.datetime(2022, 1, 10, 0, 0),
 datetime.datetime(2022, 1, 11, 0, 0),
 datetime.datetime(2022, 1, 12, 0, 0),
 datetime.datetime(2022, 1, 13, 0, 0),
 datetime.datetime(2022, 1, 14, 0, 0),
 datetime.datetime(2022, 1, 17, 0, 0),
 datetime.datetime(2022, 1, 18, 0, 0),
 datetime.datetime(2022, 1, 19, 0, 0),
 datetime.datetime(2022, 1, 20, 0, 0),
 datetime.datetime(2022, 1, 21, 0, 0),
 datetime.datetime(2022, 1, 24, 0, 0),
 datetime.datetime(2022, 1, 25, 0, 0),
 datetime.datetime(2022, 1, 27, 0, 0),
 datetime.datetime(2022, 1, 28, 0, 0),
 datetime.datetime(2022, 1, 31, 0, 0),
 datetime.datetime(2022, 2, 1, 0, 0),
 datetime.datetime(2022, 2, 2, 0, 0),
 datetime.datetime(2022, 2, 3, 0, 0),
 datetime.datetime(2022, 2, 4, 0, 0),
 datetime.datetime(2022, 2, 7, 0, 0),
 datetime.datetime(2022, 2, 8, 0, 0),
 datetime.datetime(2022, 2, 9, 0, 0),
 datetime.datetime(2022, 2, 10, 0, 0),
 datetime.datetime(2022, 2, 11, 0, 0),
 datetime.datetime(2022, 2, 14, 0, 0),
 datetime.datetime(2022, 2, 15, 0, 0),
 datetime.datetime(2022, 2, 16, 0, 0),
 datetime.datetime(2022, 2, 17, 0, 0),
 datetime.datetime(2022, 2, 18, 0, 0),
 datetime.datetime(2022, 2, 21, 0, 0),
 datetime.datetime(2022, 2, 22, 0, 0),
 datetime.datetime(2022, 2, 23, 0, 0),
 datetime.datetime(2022, 2, 24, 0, 0),
 datetime.datetime(2022, 2, 25, 0, 0),
 datetime.datetime(2022, 2, 28, 0, 0),
 datetime.datetime(2022, 3, 2, 0, 0),
 datetime.datetime(2022, 3, 3, 0, 0),
 datetime.datetime(2022, 3, 4, 0, 0),
 datetime.datetime(2022, 3, 7, 0, 0),
 datetime.datetime(2022, 3, 8, 0, 0),
 datetime.datetime(2022, 3, 9, 0, 0),
 datetime.datetime(2022, 3, 10, 0, 0),
 datetime.datetime(2022, 3, 11, 0, 0),
 datetime.datetime(2022, 3, 14, 0, 0),
 datetime.datetime(2022, 3, 15, 0, 0),
 datetime.datetime(2022, 3, 16, 0, 0),
 datetime.datetime(2022, 3, 17, 0, 0),
 datetime.datetime(2022, 3, 21, 0, 0),
 datetime.datetime(2022, 3, 22, 0, 0),
 datetime.datetime(2022, 3, 23, 0, 0),
 datetime.datetime(2022, 3, 24, 0, 0),
 datetime.datetime(2022, 3, 25, 0, 0),
 datetime.datetime(2022, 3, 28, 0, 0),
 datetime.datetime(2022, 3, 29, 0, 0),
 datetime.datetime(2022, 3, 30, 0, 0),
 datetime.datetime(2022, 3, 31, 0, 0),
 datetime.datetime(2022, 4, 1, 0, 0),
 datetime.datetime(2022, 4, 4, 0, 0),
 datetime.datetime(2022, 4, 5, 0, 0),
 datetime.datetime(2022, 4, 6, 0, 0),
 datetime.datetime(2022, 4, 7, 0, 0),
 datetime.datetime(2022, 4, 8, 0, 0),
 datetime.datetime(2022, 4, 11, 0, 0),
 datetime.datetime(2022, 4, 12, 0, 0),
 datetime.datetime(2022, 4, 13, 0, 0),
 datetime.datetime(2022, 4, 18, 0, 0),
 datetime.datetime(2022, 4, 19, 0, 0),
 datetime.datetime(2022, 4, 20, 0, 0),
 datetime.datetime(2022, 4, 21, 0, 0),
 datetime.datetime(2022, 4, 22, 0, 0),
 datetime.datetime(2022, 4, 25, 0, 0),
 datetime.datetime(2022, 4, 26, 0, 0),
 datetime.datetime(2022, 4, 27, 0, 0),
 datetime.datetime(2022, 4, 28, 0, 0),
 datetime.datetime(2022, 4, 29, 0, 0),
 datetime.datetime(2022, 5, 2, 0, 0),
 datetime.datetime(2022, 5, 4, 0, 0),
 datetime.datetime(2022, 5, 5, 0, 0),
 datetime.datetime(2022, 5, 6, 0, 0),
 datetime.datetime(2022, 5, 9, 0, 0),
 datetime.datetime(2022, 5, 10, 0, 0),
 datetime.datetime(2022, 5, 11, 0, 0),
 datetime.datetime(2022, 5, 12, 0, 0),
 datetime.datetime(2022, 5, 13, 0, 0),
 datetime.datetime(2022, 5, 16, 0, 0),
 datetime.datetime(2022, 5, 17, 0, 0),
 datetime.datetime(2022, 5, 18, 0, 0),
 datetime.datetime(2022, 5, 19, 0, 0),
 datetime.datetime(2022, 5, 20, 0, 0),
 datetime.datetime(2022, 5, 23, 0, 0),
 datetime.datetime(2022, 5, 24, 0, 0),
 datetime.datetime(2022, 5, 25, 0, 0),
 datetime.datetime(2022, 5, 26, 0, 0),
 datetime.datetime(2022, 5, 27, 0, 0),
 datetime.datetime(2022, 5, 30, 0, 0),
 datetime.datetime(2022, 5, 31, 0, 0),
 datetime.datetime(2022, 6, 1, 0, 0),
 datetime.datetime(2022, 6, 2, 0, 0),
 datetime.datetime(2022, 6, 3, 0, 0),
 datetime.datetime(2022, 6, 6, 0, 0),
 datetime.datetime(2022, 6, 7, 0, 0),
 datetime.datetime(2022, 6, 8, 0, 0),
 datetime.datetime(2022, 6, 9, 0, 0),
 datetime.datetime(2022, 6, 10, 0, 0),
 datetime.datetime(2022, 6, 13, 0, 0),
 datetime.datetime(2022, 6, 14, 0, 0),
 datetime.datetime(2022, 6, 15, 0, 0),
 datetime.datetime(2022, 6, 16, 0, 0),
 datetime.datetime(2022, 6, 17, 0, 0),
 datetime.datetime(2022, 6, 20, 0, 0),
 datetime.datetime(2022, 6, 21, 0, 0),
 datetime.datetime(2022, 6, 22, 0, 0),
 datetime.datetime(2022, 6, 23, 0, 0),
 datetime.datetime(2022, 6, 24, 0, 0),
 datetime.datetime(2022, 6, 27, 0, 0),
 datetime.datetime(2022, 6, 28, 0, 0),
 datetime.datetime(2022, 6, 29, 0, 0),
 datetime.datetime(2022, 6, 30, 0, 0),
 datetime.datetime(2022, 7, 1, 0, 0),
 datetime.datetime(2022, 7, 4, 0, 0),
 datetime.datetime(2022, 7, 5, 0, 0),
 datetime.datetime(2022, 7, 6, 0, 0),
 datetime.datetime(2022, 7, 7, 0, 0),
 datetime.datetime(2022, 7, 8, 0, 0),
 datetime.datetime(2022, 7, 11, 0, 0),
 datetime.datetime(2022, 7, 12, 0, 0),
 datetime.datetime(2022, 7, 13, 0, 0),
 datetime.datetime(2022, 7, 14, 0, 0),
 datetime.datetime(2022, 7, 15, 0, 0),
 datetime.datetime(2022, 7, 18, 0, 0),
 datetime.datetime(2022, 7, 19, 0, 0),
 datetime.datetime(2022, 7, 20, 0, 0),
 datetime.datetime(2022, 7, 21, 0, 0),
 datetime.datetime(2022, 7, 22, 0, 0),
 datetime.datetime(2022, 7, 25, 0, 0),
 datetime.datetime(2022, 7, 26, 0, 0),
 datetime.datetime(2022, 7, 27, 0, 0),
 datetime.datetime(2022, 7, 28, 0, 0),
 datetime.datetime(2022, 7, 29, 0, 0),
 datetime.datetime(2022, 8, 1, 0, 0),
 datetime.datetime(2022, 8, 2, 0, 0),
 datetime.datetime(2022, 8, 3, 0, 0),
 datetime.datetime(2022, 8, 4, 0, 0),
 datetime.datetime(2022, 8, 5, 0, 0),
 datetime.datetime(2022, 8, 8, 0, 0),
 datetime.datetime(2022, 8, 10, 0, 0),
 datetime.datetime(2022, 8, 11, 0, 0),
 datetime.datetime(2022, 8, 12, 0, 0),
 datetime.datetime(2022, 8, 16, 0, 0),
 datetime.datetime(2022, 8, 17, 0, 0),
 datetime.datetime(2022, 8, 18, 0, 0),
 datetime.datetime(2022, 8, 19, 0, 0),
 datetime.datetime(2022, 8, 22, 0, 0),
 datetime.datetime(2022, 8, 23, 0, 0),
 datetime.datetime(2022, 8, 24, 0, 0),
 datetime.datetime(2022, 8, 25, 0, 0),
 datetime.datetime(2022, 8, 26, 0, 0),
 datetime.datetime(2022, 8, 29, 0, 0),
 datetime.datetime(2022, 8, 30, 0, 0),
 datetime.datetime(2022, 9, 1, 0, 0),
 datetime.datetime(2022, 9, 2, 0, 0),
 datetime.datetime(2022, 9, 5, 0, 0),
 datetime.datetime(2022, 9, 6, 0, 0),
 datetime.datetime(2022, 9, 7, 0, 0),
 datetime.datetime(2022, 9, 8, 0, 0),
 datetime.datetime(2022, 9, 9, 0, 0),
 datetime.datetime(2022, 9, 12, 0, 0),
 datetime.datetime(2022, 9, 13, 0, 0),
 datetime.datetime(2022, 9, 14, 0, 0),
 datetime.datetime(2022, 9, 15, 0, 0),
 datetime.datetime(2022, 9, 16, 0, 0),
 datetime.datetime(2022, 9, 19, 0, 0),
 datetime.datetime(2022, 9, 20, 0, 0),
 datetime.datetime(2022, 9, 21, 0, 0)]