
import sys

input = sys.stdin.readline

word = input().rstrip()

dic = ['c=','c-', 'dz=','d-','lj','nj','s=','z=']


a = ''
count = 0
flag = False
for i in range(len(word)):
    #print('i=', i, flag)
    if(flag == True):
        flag = False
        continue
    
    
    a += word[i]

    if(len(a) == 2):
        #print(a)
        if(a in dic):
            count += 1
            a = ''
        else:
            if(i != len(word)-1):
                temp = a + word[i+1]
                #print(temp)
                if(temp in dic):
                    count += 1
                    a = ''
                    flag = True
                else:    
                    count += 1
                    a = a[1:]
            else:
                count += 1
                a = a[1:]

    #print(count)  

if(a != ''):
    count += 1

print(count) 