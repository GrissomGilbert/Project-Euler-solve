'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import time

dict_arr={'and':len('and'),1:len("one"),2:len('two'),3:len('three'),4:len('four'),5:len('five'),\
          6:len('six'),7:len('seven'),8:len('eight'),9:len('nine'),10:len('ten'),11:len('eleven'),\
          12:len('twelve'),13:len('thirteen'),14:len('fourteen'),15:len('fifteen'),16:len('sixteen'),\
          17:len('seventeen'),18:len('eighteen'),19:len('nineteen'),20:len('twenty'),30:len('thirty'),\
          40:len('forty'),50:len('fifty'),60:len('sixty'),70:len('seventy'),80:len('eighty'),90:len('ninety'),\
          100:len('hundred'),1000:len('thousand')}

if __name__ == '__main__':
    digit_sum=0
    run_time=time.time()
    for m in range(1,1001):
        tmp_val=0
        base=m
        divider = 1000
        while divider!=0 and base!=0:
            if divider==10 and int(m/100)!=0:
                digit_sum+=dict_arr['and']
            if m<100:
                divider=10
            if base<20:
                digit_sum+=dict_arr[base]
                break
            elif divider==10:
                if base%divider==0:
                    digit_sum+=dict_arr[base]
                else:
                    digit_sum+=dict_arr[int(base/divider)*10]
                    digit_sum+=dict_arr[base%divider]
                break
            elif divider==100 and int(base/divider)!=0:
                digit_sum+=dict_arr[int(base/divider)]
                digit_sum+=dict_arr[divider]
            elif divider==1000 and int(base/divider)!=0:
                digit_sum+=dict_arr[int(base/divider)]
                digit_sum+=dict_arr[divider]
            base=base%divider
            divider=int(divider/10)
    run_time=time.time()-run_time
    print("calculation time %f"%run_time)
    print("all the numbers from 1 to 1000 used %d letters in total"%digit_sum)