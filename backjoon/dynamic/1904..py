
import sys

input = sys.stdin.readline

n = int(input())

nums = [0] * 1000001
nums[1] = 1
nums[2] = 2

for i in range(3, n+1):

    nums[i] = (nums[i-2] + nums[i-1])%15746


print(nums[n])

    