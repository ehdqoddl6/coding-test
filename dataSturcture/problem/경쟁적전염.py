import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

def solution(graph, s, x, y):

   

    index = [[] for _ in range(k+1)]
    
    for i in range(n):
        for j in range(n):
            
            if(graph[i][j] != 0):
                index[graph[i][j]].append((i,j))


    queue = deque()

    for i in index:
        for j in range(len(i)):
            queue.append(i[j])



    count = 0
    
    side = [0, 0, -1, 1]
    up = [1, -1, 0, 0] 

    while(count != s):

        num = len(queue)

        for i in range(num):

            a = queue.popleft()          
            x1, y1 = a[0], a[1]
            
            for j in range(len(side)):

                nx = x1 + side[j]
                ny = y1 + up[j]

                if(nx < 0 or nx>=n or ny<0 or ny>=n):
                    continue
                
                else:
                    if(graph[nx][ny] == 0):
                       
                        graph[nx][ny] = graph[x1][y1]
                        queue.append((nx, ny))
                
        count += 1
    
    return graph[x-1][y-1]
    

    
    
            
        
        

    


print(solution(graph, s, x, y))