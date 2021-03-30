import heapq
import sys

input = sys.stdin.readline

n = int(input())

result = []
h = []

for i in range(n):
    x = int(input())

    if(x == 0):
        if(len(h) == 0):
            result.append(0)
        
        else:
            a = heapq.heappop(h)
            result.append(a[1])

    else:
        heapq.heappush(h, (abs(x), x))



for x in result:
    print(x)