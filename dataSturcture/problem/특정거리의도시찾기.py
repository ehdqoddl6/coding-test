
import sys

input = sys.stdin.readline

#n, m, k, x = map(int, input().split())
n, m, k, x = 4,4,2,1

graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
print(n,m,k,x)
"""
for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
"""
graph = [
    [],
    [2,3],
    [3,4],
    [],
    []
]

from collections import deque

def solution(graph, k, x):
    
    queue = deque([x])
    print(queue)
    distance[x] = 0
    
    while(queue):
        print(distance)
        now = queue.popleft()
        print(now)
        for i in graph[now]:

            if(distance[i] == -1):
                distance[i] = distance[now] + 1
                queue.append(i)

    check = False

    for i in range(1, n+1):
        if(distance[i] == k):
            print(i)
            check = True

    if(check == False):
        print(-1)


solution(graph, k, x)
