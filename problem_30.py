'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

from time import time

if __name__ == '__main__':
    cal_time=time()
    sum=0
    limit=354294
    power=5
    divider=10
    for m in range(100,limit):
        tmp_val=m
        power_sum=0
        while tmp_val!=0:
            remainder=tmp_val%divider
            tmp_val=int(tmp_val/divider)
            power_sum+=remainder**power
        if m==power_sum:
            sum+=m
    print("the sum of all the numbers is %d"%sum)
    print("calculation time is %f"%(time()-cal_time))