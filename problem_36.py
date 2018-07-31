'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
from _functools import reduce
from time import time

def is_Palindrome(n,base):
    reversed=0
    tmp=n
    while tmp>0:
        reversed=base*reversed+tmp%base
        tmp=tmp//base
    return n==reversed

if __name__ == '__main__':
    cal_time=time()
    upper_bound=1000000
    sum=0
    for m in range(1,upper_bound,2):
        if is_Palindrome(m,10) and is_Palindrome(m,2):
            sum+=m
    print("the sum of all numbers, less than one million is %d"%sum)
    print("calculation time is %f"%(time()-cal_time))