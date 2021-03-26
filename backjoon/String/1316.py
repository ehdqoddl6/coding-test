import sys

input = sys.stdin.readline

n = int(input())

word = []
for _ in range(n):
    word.append(input())



def solution(word):

    count = 0

    for x in word:

        dic = []
        previous = ''


        for i in range(len(x)):

            if(previous != x[i] and x[i] not in dic):
                dic.append(x[i])
            elif(previous == x[i] and x[i] in dic):
                continue
            else:
                break
            
            if(i == len(x)-1):
                
                count += 1

            previous = x[i]
        
        
    return count

print(solution(word))