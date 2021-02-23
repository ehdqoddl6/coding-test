"""
인접행렬(adjacency Matrix) : 2차원 배열로 그래프의 연결관계를 표현항 방식
모든 관계를 저장하기 때문에 불필요한 메모리 생김

인접리스트 (adjacency List) : 리스트로 그래프의 연결관계를 표현하는 방식
연결된 정보만을 저장하기 떄문에 메모리 효율적으로 사용가능
하지만, 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가느리다.
"""

INF = 999999999

#adjacency Matrix
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

#adjacency List
graph = [[] for _ in range(3)]

print(graph)

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)



