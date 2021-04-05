import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lamps = []
for _ in range(n):
    lamps.append(input())

k = int(input())


def solution(lamps, k):
    count = 0

    for i in range(k):

        for j in range(n):

            for l in range(m):
                

    return count




print(solution(lamps, k))