'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

from time import time

def get_prime_sieve(sieve_limit):
    sieve_list=[True for m in range(0,sieve_limit)]
    for m in range(3,sieve_limit):
        if sieve_list[m]==False:
            continue
        count=2
        while m*count <sieve_limit:
            sieve_list[m*count]=False
            count+=1
    return sieve_list

def circular_count(num,sieve_list):
    tmp=num
    count=1
    divider=10
    divider_counts=0
    while True:
        tmp=tmp//divider
        if tmp == 0:
            break
        divider_counts+=1
    tmp=num
    while True:
        tmp_val=tmp%divider
        tmp=tmp//divider
        tmp=tmp_val*(divider**divider_counts)+tmp
        if not sieve_list[tmp]:
            return False,count
        if tmp==num:
            if count == 1:
                return True,count
            break
        sieve_list[tmp]=False
        count+=1
    return True,count

if __name__ == '__main__':
    cal_time=time()
    upper_bound=1000000
    sums=1
    sieve_list=get_prime_sieve(upper_bound)
    for m in range(3,upper_bound,2):
        if not sieve_list[m]:
            continue
        ret,num=circular_count(m, sieve_list)
        if ret:
            sums+=num
    print("below one million there are %d circular primes"%sums)
    print("calculation time is %f"%(time()-cal_time))