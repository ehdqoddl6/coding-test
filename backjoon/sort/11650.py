import sys

n = int(input())

nums = []
for i in range(n):
    a, b = map(int, input().split())
    nums.append([a, b])

"""
nums = [
    [3, 4],
    [1, 1],
    [1, -1],
    [2, 2],
    [3, 3]
]
"""


def solution(array):

    array.sort()
    return array

result = solution(nums)

for x in result:
    print(x[0], x[1])