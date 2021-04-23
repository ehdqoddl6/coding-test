
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * n
result = []


for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(m):

            if(i == j):
                continue

            result.append((i,j))

for x in result:
    print(x)

def solution(start, n, m):

    if(start == m):
solution(0, n, m)