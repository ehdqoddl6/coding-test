
import sys
n = int(input())

stack = []

result = []

for i in range(n):
    input_data = sys.stdin.readline().rstrip()
    a = input_data.split()

    if(len(a) == 2):
        stack.append(int(a[1]))

    else:
        if(a[0] == 'top'):
            if(len(stack) == 0):
                result.append(-1)
            else:
                result.append(stack[-1])
            

        elif(a[0] == 'size'):
            result.append(len(stack))
            
        
        elif(a[0] == 'pop'):
            if(len(stack) == 0):
                result.append(-1)
            else:
                a = stack.pop()
                result.append(a)
        
        elif(a[0] == 'empty'):
            if(len(stack) >= 1):
                result.append(0)
            
            else:
                result.append(1)


for i in result:
    print(i)