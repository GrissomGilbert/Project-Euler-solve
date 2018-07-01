'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
'''

import time

data_str='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

if __name__ == '__main__':
    data_arr=[x.split(" ") for x in data_str.split("\n")]
    max_sum=0
    cal_time=time.time()
    for m in range(0,len(data_arr)-1):
        tmp_val=int(data_arr[m+1][0])
        for n in range(0,len(data_arr[m])):
            data_arr[m+1][n]=str(max(int(data_arr[m+1][n]),tmp_val+int(data_arr[m][n])))
            tmp_val=int(data_arr[m+1][n+1])
            data_arr[m+1][n+1]=str(int(data_arr[m][n])+int(data_arr[m+1][n+1]))
    for m in range(0,len(data_arr[-1])):
        max_sum=int(max(max_sum,int(data_arr[-1][m])))
    print("calculate time %f"%(time.time()-cal_time))
    print("the maximum total from top to bottom is %d"%max_sum)