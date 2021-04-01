import sys

input = sys.stdin.readline
n = int(input())

nums = list(map(int, input().split()))

def solution(nums):

    result = [nums[0]]

    for i in range(len(nums)-1):
        result.append(max(result[i] + nums[i+1], nums[i+1]))

    return result


print(max(solution(nums)))