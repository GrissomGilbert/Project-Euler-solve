'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''
from time import time

def get_Power_Sum(base,exponent):
    digit_arr=[]
    digit_arr.append(base)
    tmp_val=0
    for m in range(2,exponent+1):
        carry_over=0
        for n in range(len(digit_arr)-1,-1,-1):
            tmp_val=digit_arr[n]*base+carry_over
            carry_over=int(tmp_val/10)
            digit_arr[n]=tmp_val%10
        if carry_over!=0:
            digit_arr.insert(0, carry_over)
    sum=0
    for digit in digit_arr:
        sum+=digit
    return sum

if __name__ == '__main__':
    cal_time=time()
    print("the sum of the digits of the number 2^1000 is %d"%get_Power_Sum(2,1000))
    print("calculation time is %f"%(time()-cal_time))