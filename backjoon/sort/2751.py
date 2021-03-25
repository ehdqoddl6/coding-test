import sys

input = sys.stdin.readline

n = int(input())

num = []
for i in range(n):
    num.append(int(input()))

import heapq

def solution(array):

    h = []

    for x in array:
        heapq.heappush(h, x)

    result = []

    while(h):
        result.append(heapq.heappop(h))

    return result

    

num = solution(num)

for x in num:
    print(x)

