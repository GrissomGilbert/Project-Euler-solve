'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
from _functools import reduce
from time import time

def is_curious(num,pro_dict):
    tmp=num
    sum=0
    divider=10
    while tmp!=0:
        sum+=pro_dict[tmp%divider]
        tmp=tmp//divider
    if sum==num:
        return True
    return False

if __name__ == '__main__':
    cal_time=time()
    product_dict={}
    upper=0
    for m in range(0,10):
        product_dict[m]=reduce(lambda x,y:x*y,range(1,m+1),1)
        upper+=product_dict[m]
    product_dict[0]=1
    sum=0
    for m in range(3,upper):
        if is_curious(m, product_dict):
            sum+=m
    print("the sum of all numbers which are equal to the sum of the factorial of their digits is %d"%sum)
    print("calculation time is %f"%(time()-cal_time))