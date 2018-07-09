'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import time

def factorial(num):
    sum=1
    for m in range(1,num+1):
        sum*=m
    return sum

if __name__ == '__main__':
    cal_time=time.time()
    digits=[x for x in range(0,10)]
    sum=999999
    result=[]
    n=9
    while sum!=0:
        x=factorial(n)
        index=int(sum/x)
        result.append(digits[index])
        digits.pop(index)
        sum=sum%x
        n-=1
    result.append(digits[0])
    print("the millionth lexicographic permutation of the digits is %s"%result)
    print("calculate time is %f"%float(time.time()-cal_time))
    
'''
0*********
0-123456789 (1 th)
0-987654321 (9! = 362880 th)

1*********
1-023456789 (9! + 1 = 362881 th)
1-987654320 (9! + 9! = 725760 th)

2*********
2-013456789 (9! + 9! + 1)
2-987654310 (9! + 9! + 9! = 1088640 th)

So, 2013456789 < 1M th < 2987654310

2013456789 (9! + 9! + 1 = 725761 th)

We keep '2' permute  remain numbers: 2*********
We repeat above steps util value of permutation not less than 1000,000:
20-13456789 (2*9! + 1 = 725761 th)
20-98765431 (2*9! + 8!)
21-03456789 (2*9! + 8! + 1)
21-98765430 (2*9! + 8! + 8!)
23-01456789 (2*9! + 8! + 8! + 1)
23-98765410 (2*9! + 8! + 8! + 8!)
24-01356789 (2*9! + 3*8! + 1)
24-98765310 (2*9! + 3*8! + 8! = 887040)
25-01346789 (2*9! + 4*8! + 1 = 887041)
25-98764310 (2*9! + 4*8! + 8! = 927360)
26-01345789 (2*9! + 5*8! + 1 = 927360)
26-98754310 (2*9! + 5*8! + 8! = 967680)
...
27-98754310 (2*9! + 6*8! = 1008000)

So, 2701345689 < x < 2798654310

So on, we have:

2*9! + 6*8! + 6*7! + 2*6! + 5*5! + 1*4! + 2*3! + 1*2! + 1*1! + 1*0! = 1000000  (I)

By (I), We have:
pick 2th (number 2) from [0123456789] , remain [01 3456789]
pick 6th (number 7) from [01 3456789] , remain [01 3456 89]
pick 6th (number 8) from [01 3456 89] , remain [01 3456  9]
pick 2th (number 3) from [01 3456  9] , remain [01  456  9]
pick 5th (number 9) from [01  456  9] , remain [01  456   ]
pick 1th (number 1) from [01  456   ] , remain [0   456   ]
pick 2th (number 5) from [0   456   ] , remain [0   4 6   ]
pick 1th (number 4) from [0   4 6   ] , remain [0     6   ]
pick 1th (number 6) from [0     6   ] , remain [0         ]
pick      number 0

=> 2783915460
'''