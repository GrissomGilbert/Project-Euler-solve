'''
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out
the alphabetical value for each name, multiply this value by
its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import time


def get_content_list(file_path):
    with open(file_path) as f:
        content=f.read()
        content=content.replace("\"",'')
        name_list=content.split(',')
    return name_list

if __name__ == '__main__':
    cal_time=time.time()
    scores=0
    count=1
    name_list=get_content_list('./p022_names.txt')
    name_list.sort()
    for name in name_list:
        name_score=0
        name=name.lower()
        for m in name:
            name_score=name_score+ord(m)-ord('a')+1
        name_score*=count
        scores+=name_score
        count+=1
    print("calculate time is %f"%(time.time()-cal_time))
    print("the total of all the name scores in the file is %d"%scores)