import sys


input = sys.stdin.readline
n = int(input())

zero = [1,0,1]
one = [0,1,1]

def solution(num):
    
    if(num >= len(zero)):

        for i in range(len(zero), num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
        
    
    return (zero[num], one[num])
   



result = []
for _ in range(n):

    num = int(input())

    result.append(solution(num))

for x in result:
    print(x[0], x[1])
   