'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

from decimal import Decimal
from _decimal import getcontext
import time

def get_recurring(data_list):
    pivot=0
    recur_list=[data_list[pivot]]
    data_str=''.join(data_list)
    recurring=0
    count=0
    while count<len(data_list):
        if count>int(len(data_list)/2):
            break
        if not data_list[pivot] in data_list[count:]:
            pivot=count
            recur_list=[data_list[pivot]]
            continue
        else:
            loc=data_str.find(''.join(recur_list),count)
            if loc!=-1:
                if loc==count:
                    count=loc+len(recur_list)
                    pivot=count
                    continue
                recur_list.append(data_list[count])
                recurring=max(recurring,len(recur_list))
            else:
                break
        count+=1
    return recurring

if __name__ == '__main__':
    cal_time=time.time()
    limit=1000
    count=3
    longest_recur=0
    value=0
    getcontext().prec=2000
    while count<limit:
        remainder=str(Decimal(1)/Decimal(count))
        data_list=list(remainder)
        data_list=data_list[2:]
        tmp_val=get_recurring(data_list)
        if tmp_val>longest_recur:
            longest_recur=tmp_val
            value=count
        count+=2
    print("the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is %d"%value)
    print("calculation time is %f"%(time.time()-cal_time))