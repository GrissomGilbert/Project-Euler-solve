'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt
from math import floor
import time

def get_divisors_sum(num):
    if num==1:
        return 0
    sum=1
    start=2
    step=1
    r=floor(sqrt(num))
    if r**2==num:
        sum=1+r
        r=r-1
    if num%2!=0:
        start=3
        step=2
    for m in range(start,r+1,step):
        if num%m==0:
            sum=sum+m+int(num/m)
    return sum

if __name__ == '__main__':
    cal_time=time.time()
    sum=0
    limit=10000
    for m in range(2,limit):
        counter_part=get_divisors_sum(m)
        if counter_part>m:
            if m==get_divisors_sum(counter_part):
                sum=sum+m+counter_part
    print("calculate time is %f"%(time.time()-cal_time))
    print("the sum of all the amicable numbers under 10000 is %d"%sum)