
import sys

n = int(sys.stdin.readline())

k = 10

nums = []

while(n > 0):
    
    a = n % k
    nums.append(a)

    n = n // k


nums.sort(reverse=True)

for x in nums:
    print(x, end='')