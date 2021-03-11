import sys

n = int(input())

nums = []
for i in range(n):
    a, b = map(int, input().split())
    nums.append([b, a])


def solution(array):

    array.sort()
    return array

result = solution(nums)



for x in result:
    print(x[1], x[0])