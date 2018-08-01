'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

from time import time
from math import sqrt
from math import floor

def get_the_prime(target):
    prim_arr=[2]
    count_val=3
    while(len(prim_arr)<target):
        is_prim=True
        for prim in range(3,floor(sqrt(count_val))+1):
            if(count_val%prim==0):
                is_prim=False
                break
        if(is_prim):
            prim_arr.append(count_val)
        count_val+=2
    return count_val-2

if __name__ == '__main__':
    cal_time=time()
    print("The 10001st prim is %d"%get_the_prime(10001))
    print("calculation time is %f"%(time()-cal_time))