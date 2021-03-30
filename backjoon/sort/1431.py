import sys

input = sys.stdin.readline


nums = []
n = int(input())

for _ in range(n):
    
    a = input().rstrip()

    digit_sum = 0
    alpha = ''
    for x in a:
        if(x >= '0' and x<='9'):
            digit_sum += int(x)
        else:
            alpha += x

    nums.append((a, len(a), digit_sum, alpha))

nums = sorted(nums, key=lambda x:(x[1], x[2], x[0]))

for x in nums:
    print(x[0])