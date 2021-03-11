import sys

n = int(input())

nums = []
for i in range(n):
    a, b = map(int, input().split())
    nums.append([a, b])


def solution(array):

    array.sort()
    return array

result = solution(nums)

for x in result:
    print(x[0], x[1])