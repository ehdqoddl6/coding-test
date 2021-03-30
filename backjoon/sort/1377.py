import sys

input = sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    nums.append((int(input()), i))

sorted_nums = sorted(nums)
answer = []

for i in range(n):
    answer.append(sorted_nums[i][1] - nums[i][1])


print(max(answer) + 1)