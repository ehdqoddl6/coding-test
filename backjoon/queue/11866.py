
from collections import deque

n, k = map(int, input().split())

def solution (n, k):

    person = deque(i+1 for i in range(n))

    print('<', end='')
    while(person):

        for i in range(k-1):
            
            a = person.popleft()
            person.append(a)

        print(person.popleft(), end='')
        
        if(person):
            print(',', end=' ')
       
    print('>', end='')


solution(n, k)
