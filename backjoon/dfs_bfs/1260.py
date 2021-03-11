
n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def dfs(graph, v, visited):
    visited[v] = True
    
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n+1)
dfs(graph, start, visited)

from collections import deque
def bfs(graph, v, visited):

    queue = deque()
    queue.append(start)

    visited[start] = True

    while queue:

        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print()
visited = [False] * (n+1)
bfs(graph, start, visited)