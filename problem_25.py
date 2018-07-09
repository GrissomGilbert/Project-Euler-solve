'''
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

import time

def gerator_fibonacci(digits):
    limit = 0
    value_actual = 2
    fibs = [1,1,2]
    counter = 3
    while limit < digits:
        counter += 1
        value_actual = value_actual + fibs[-2]
        fibs.append(value_actual)
        limit = len(str(value_actual))
    return counter

if __name__ == '__main__':
    cal_time = time.time()
    print("the index of the first term in the Fibonacci sequence to contain 1000 digits is %d"%gerator_fibonacci(1000))
    print("calculation time is %f"%(time.time() - cal_time))

'''
The fibonacci number sequence is given by the following recurrence : F(n) = F(n-1) + F(n-2) Via the study of such sequence,
it’s easy to prove that F(n) = 1/sqrt(5) * (phi^n - psi^n) where phi = (1+sqrt(5))/2, psi = (1-sqrt(5))/2 Since p = |phi/psi| < 1,
log F(n) = n*log(phi) - log(5)/2 + O(p^n) So very quickly, the approximation log(F(n)) = n*log(phi) - log(5)/2 becomes accurate enough
(p^n decreases geometrically) So if log(F(n)) >= 999 then n >= (999+log(5)/2)/log(phi) ~ 4781.9, so the answer must be 4782. 
'''