
import sys
from collections import deque

queue = deque()

n = int(input())
result = []

for i in range(n):
    input_data = sys.stdin.readline().rstrip()
    a = input_data.split()

    if(len(a) == 2):
        if(a[0] == 'push_back'):
            queue.append(int(a[1]))
        else:
            queue.appendleft(int(a[1]))

    else:
        if(a[0] == 'back'):
            if(len(queue) == 0):
                result.append(-1)
            else:
                result.append(queue[-1])
        
        elif(a[0] == 'front'):
            if(len(queue) == 0):
                result.append(-1)
            else:
                result.append(queue[0])
            

        elif(a[0] == 'size'):
            result.append(len(queue))
            
        
        elif(a[0] == 'pop_front'):
            if(len(queue) == 0):
                result.append(-1)
                
            else:
                a = queue.popleft()
                result.append(a)

        elif(a[0] == 'pop_back'):
            if(len(queue) == 0):
                result.append(-1)
                
            else:
                a = queue.pop()
                result.append(a)

        elif(a[0] == 'empty'):
            if(len(queue) >= 1):
                result.append(0)
            
            else:
                result.append(1)
        


for i in result:
    print(i)
