'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

from time import time

if __name__ == '__main__':
    cal_time=time()
    limit=1001**2
    sum=1
    step=2
    count=0
    m=3
    while m<=limit:
        sum+=m
        count+=1
        if count==4:
            count=0
            step+=2
        m+=step
    print("the sum of the numbers on the diagonals in a 1001 by 1001 spiral is %d"%sum)
    print("calculation time is %f"%(time()-cal_time))