
vex = int(input())
node = int(input())

graph = [[] for i in range(vex+1)]

for i in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    graph[a].sort()
    graph[b].sort()

result = []
def dfs(graph, v, visited):
    visited[v] = True

    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False]*(vex+1)
dfs(graph, 1, visited)

print(len(result) - 1)