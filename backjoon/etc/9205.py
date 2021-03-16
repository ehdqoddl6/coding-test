
from collections import deque
n = int(input())


def solution(x, y):

    queue = deque()
    visited = []

    queue.append([x,y])
    visited.append([x,y])

    while(queue):
        x, y = queue.popleft()
        if(x == x_end and y == y_end):
            return 'happy'
        
        for nx, ny in loc:
            if([nx, ny] not in visited):
                distance = abs(nx-x) + abs(ny-y)
                if(distance <= 1000):
                    queue.append([nx, ny])
                    visited.append([nx, ny]) 
    
    return 'sad'

result = []
for i in range(n):

    loc = []
    con = int(input())
    x_start, y_start = map(int, input().split())
    
    for j in range(con):
        x, y = map(int, input().split())
        loc.append([x, y])

    x_end, y_end = map(int, input().split())
    loc.append([x_end, y_end])
    
    result.append(solution(x_start, y_start))


for x in result:
    print(x)
