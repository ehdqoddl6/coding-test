
k = int(input())


stack = []

for i in range(k):

    n = int(input())

    if(n == 0):
        if(len(stack) != 0):
            stack.pop()

    else:
        stack.append(n)
        
print(sum(stack))