#heap sort를 이용해서 풀이
import sys
import heapq

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))


def solution(array):

    h = []

    for x in array:
        heapq.heappush(h, x)

    sum = 0

    while(len(h) != 1):
        

        a = heapq.heappop(h)
        b = heapq.heappop(h)
        sum += (a + b)

        

        heapq.heappush(h, a+b)

    
    return sum


print(solution(array))