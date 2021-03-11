
import sys

n = int(sys.stdin.readline())

dict = []
for i in range(n):
    dict.append(input())


dic = []

for x in dict:
    if(x not in dic):
        dic.append(x)


result = []

max_len = 0
for x in dic:
    if(max_len < len(x)):
        max_len = len(x)


for i in range(max_len+1):
    temp_dic = []

    for x in dic:
        if(len(x) == i):
            temp_dic.append(x)
    
    temp_dic.sort()

    for x in temp_dic:
        result.append(x)


for x in result:
    print(x)
