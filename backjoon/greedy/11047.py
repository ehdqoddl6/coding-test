import sys

input = sys.stdin.readline


n, k = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))


count = 0
for x in range(n-1, -1, -1):
    
    if(k >= nums[x]):
        a = k // nums[x]
        count += a
        k = k - a*nums[x]

    

print(count)
