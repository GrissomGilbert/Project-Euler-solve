'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

from time import time

def get_prime_sieve(sieve_limit):
    sieve_list=[True for m in range(0,sieve_limit)]
    sieve_list[0]=False
    sieve_list[1]=False
    for m in range(2,sieve_limit):
        if sieve_list[m]==False:
            continue
        count=2
        while m*count <sieve_limit:
            sieve_list[m*count]=False
            count+=1
    return sieve_list

def is_truncate(val,prime_list):
    if not prime_list[val]:
        return False
    back=val//10
    front=int(str(val)[1:])
    while True:
        if not prime_list[back]:
            return False
        if not prime_list[front]:
            return False
        back=back//10
        if back==0:
            break
        front=int(str(front)[1:])
    return True
if __name__ == '__main__':
    cal_time=time()
    k=23
    sums=0
    round=0
    upper_bound=1000000
    prime_list=get_prime_sieve(upper_bound)
    while round<11:
        if is_truncate(k,prime_list):
            sums+=k
            round+=1
        k+=2
    print("The sum of first eleven truncatable primes is %d"%sums)
    print("calculation time is %f"%(time()-cal_time))
