'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

from time import time

coin_list=[200,100,50,20,10,5,2,1]

def get_coin_count(value, coin, coin_index):
    sum=0
    if coin_index==len(coin_list)-1:
        return 1
    for m in range(coin_index,len(coin_list)):
        difference= value-coin_list[m]
        if difference==0:
            sum+=1
        if difference>0:
            sum+=get_coin_count(difference, coin_list[m], m)
    return sum
if __name__ == '__main__':
    cal_time = time()
    combs_sum=get_coin_count(200, coin_list[0], 0)
    print("The total ways of £2 be made using any number of coins is %d"%combs_sum)
    print("calculation time is %f"%(time()-cal_time))