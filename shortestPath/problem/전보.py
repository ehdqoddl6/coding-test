import heapq
import sys

input = sys.stdin.readline

INF = 1e10

n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))


def solution(start):

    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while(q):
        
        dist, now = heapq.heappop(q)

        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if(cost < distance[i[0]]):
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
solution(start)

count = 0
max_distance = 0

for x in distance:

    if(x != INF):
        count += 1
        max_distance = max(max_distance, x)

print(count-1, max_distance)


