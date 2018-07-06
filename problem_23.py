'''
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n. As 12 is the smallest
abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.
'''

from math import floor
from math import sqrt
import time

def get_divisors_sum(num):
    if num==1:
        return 1
    start=2
    step=1
    sum=1
    r=floor(sqrt(num))
    if r**2==num:
        sum=1+r
        r-=1
    if num%2!=0:
        start+=1
        step+=1
    for m in range(start,r+1,step):
        if num%m==0:
            sum=sum+m+int(num/m)
    return sum

if __name__ == '__main__':
    cal_time=time.time()
    limit=28124
    total_sum=0
    abundant_sum=0
    abundant_set=set()
    possible_sum={}
    for m in range(1,limit):
        if m<get_divisors_sum(m):
            abundant_set.add(m)
        if not any((m-j) in abundant_set for j in abundant_set):
            total_sum+=m
    print("the sum of all the positive integers which cannot be written as\
the sum of two abundant numbers is %d"%total_sum)
    print("calculate time is %f"%(time.time()-cal_time))
