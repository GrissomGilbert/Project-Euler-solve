'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import time

month_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

if __name__ == '__main__':
    days_count=366
    monday_count=0
    cal_time=time.time()
    for year in range(1901,2001):
        for month in range(1,13):
            if days_count%7==1:
                monday_count+=1
            days_count+=month_dict[month]
            if month==2 and year%4==0:
                if year%400!=0:
                    pass
                else:
                    days_count+=1
    print("calculate time %f"%(time.time()-cal_time))
    print("%d days fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)"%monday_count)