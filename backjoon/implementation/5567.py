import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())


friend = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

def bfs(x):
    q = deque()
    visited = [0] * n
    visited[x] = 1
    q.append(x)

    while q:
        x = q.popleft()
        for i in friend[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    return visited



cnt = 0

res = bfs(0)
for res_ in res:
    if 1 < res_ <= 3:
        cnt += 1
print(cnt)



