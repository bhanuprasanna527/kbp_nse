import datetime
from datetime import date

def get_interval(year_from: int, month_from: int):
        
    hol2019 = [
        datetime.datetime(2019, 3, 4, 0, 0),
        datetime.datetime(2019, 3, 21, 0, 0),
        datetime.datetime(2019, 4, 17, 0, 0),
        datetime.datetime(2019, 4, 19, 0, 0),
        datetime.datetime(2019, 5, 1, 0, 0),
        datetime.datetime(2019, 6, 5, 0, 0),
        datetime.datetime(2019, 8, 12, 0, 0),
        datetime.datetime(2019, 8, 15, 0, 0),
        datetime.datetime(2019, 9, 2, 0, 0),
        datetime.datetime(2019, 9, 10, 0, 0),
        datetime.datetime(2019, 10, 2, 0, 0),
        datetime.datetime(2019, 10, 8, 0, 0),
        datetime.datetime(2019, 10, 28, 0, 0),
        datetime.datetime(2019, 11, 12, 0, 0),
        datetime.datetime(2019, 12, 25, 0, 0)
    ]

    hol2020 = [
        datetime.datetime(2020, 2, 21, 0, 0),
        datetime.datetime(2020, 3, 10, 0, 0),
        datetime.datetime(2020, 4, 2, 0, 0),
        datetime.datetime(2020, 4, 6, 0, 0),
        datetime.datetime(2020, 4, 10, 0, 0),
        datetime.datetime(2020, 4, 14, 0, 0),
        datetime.datetime(2020, 5, 1, 0, 0),
        datetime.datetime(2020, 5, 25, 0, 0),
        datetime.datetime(2020, 10, 2, 0, 0),
        datetime.datetime(2020, 11, 16, 0, 0),
        datetime.datetime(2020, 11, 30, 0, 0),
        datetime.datetime(2020, 11, 25, 0, 0)
    ]

    hol2022 = [
        datetime.datetime(2022, 1, 26, 0, 0),
        datetime.datetime(2022, 3, 1, 0, 0),
        datetime.datetime(2022, 3, 18, 0, 0),
        datetime.datetime(2022, 4, 14, 0, 0),
        datetime.datetime(2022, 4, 15, 0, 0),
        datetime.datetime(2022, 5, 3, 0, 0),
        datetime.datetime(2022, 8, 9, 0, 0),
        datetime.datetime(2022, 8, 15, 0, 0),
        datetime.datetime(2022, 8, 31, 0, 0),
        datetime.datetime(2022, 10, 5, 0, 0),
        datetime.datetime(2022, 10, 24, 0, 0),
        datetime.datetime(2022, 10, 26, 0, 0),
        datetime.datetime(2022, 11, 8, 0, 0)
    ]

    hol2021 = [
        datetime.datetime(2021, 1, 26, 0, 0),
        datetime.datetime(2021, 3, 11, 0, 0),
        datetime.datetime(2021, 3, 29, 0, 0),
        datetime.datetime(2021, 4, 2, 0, 0),
        datetime.datetime(2021, 4, 14, 0, 0),
        datetime.datetime(2021, 4, 21, 0, 0),
        datetime.datetime(2021, 5, 13, 0, 0),
        datetime.datetime(2021, 7, 21, 0, 0),
        datetime.datetime(2021, 8, 19, 0, 0),
        datetime.datetime(2021, 9, 10, 0, 0),
        datetime.datetime(2021, 10, 15, 0, 0),
        datetime.datetime(2021, 11, 4, 0, 0),
        datetime.datetime(2021, 11, 5, 0, 0),
        datetime.datetime(2021, 11, 19, 0, 0)
    ]

    ex_hol = []

    leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    nleap = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


    today = date.today()
    d = int(today.day)
    m = int(today.month)
    y = int(today.year)-2000

    for i in range(year_from,y+1):
        if i == y:
            month_to = m
        else:
            month_to = 12
        yearstr = str(i)
        if i == year_from:
            mf = month_from
        else:
            mf = 1
        for j in range(mf, month_to+1):
            if j == month_to:
                days_range = d-1
            else:
                if i == 20:
                    days_range = leap[j]
                else:
                    days_range = nleap[j]
            monthstr = ""
            if j < 10:
                monthstr = "0" + str(j)
            else:
                monthstr = str(j)
            for k in range(1, days_range+1):
                daystr = ""
                if k < 10:
                    daystr = "0" + str(k)
                else:
                    daystr = str(k)
                fin_date = datetime.datetime(int("20{y}".format(y = i)), j, k)
                if fin_date in hol2020:
                    print(True)
                if fin_date.weekday() <= 4 and fin_date not in hol2022 and fin_date not in hol2021 and fin_date not in hol2020 and fin_date not in hol2019:
                    ex_hol.append(fin_date)
    return ex_hol