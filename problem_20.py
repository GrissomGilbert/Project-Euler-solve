'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time

def get_digits_sum(max_limit):
    data_arr=[0 for m in range(0,500)]
    data_arr[-1]=1
    tmp_val=0
    sum=0
    reminder=0
    divider=10
    for m in range(2,max_limit+1):
        for n in range(len(data_arr)-1,-1,-1):
            tmp_val=m*data_arr[n]+reminder
            data_arr[n]=tmp_val%divider
            reminder=int(tmp_val/divider)
    for data in data_arr:
        sum+=data
    return sum

if __name__ == '__main__':
    calc_time=time.time()
    print("the sum of the digits in the number 100 is %d"%get_digits_sum(100))
    print("calculation time is %f"%(time.time()-calc_time))
        