
import sys

input = sys.stdin.readline

t = int(input())

nums = [0] * 101
a = [0,1,1,1,2,2,3,4,5,7,9]
for i in range(len(a)):
    nums[i] = a[i]

result = []
for i in range(t):

    n = int(input())

    if(n <= 10):
        result.append(nums[n])
    else:
        for i in range(11, n+1):
            nums[i] = nums[i-1] + nums[i-5]
        
        result.append(nums[n])


for x in result:
    print(x)