
import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))


stack = []
result = []
a = []
j = 0
for i in range(1, n+1):
    
    if(len(stack) == 0 or stack[-1] != nums[j]):
        stack.append(i)
        result.append('+')
    
    else:
        
    
        while(len(stack) != 0 and nums[j] == stack[-1]):
            a.append(stack.pop())
            result.append('-')
            j += 1
        
        stack.append(i)
        result.append('+')

   

while(stack):

    a.append(stack.pop())
    result.append('-')
    j += 1


if(a == nums):
    for x in result:
        print(x)
else:
    print('NO')