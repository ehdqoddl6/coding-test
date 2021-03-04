
n = int(input())

array = list(map(int, input().split()))

def solve(array):

    result = []

    for i in range(n):
    
        if(i == (n-1)):
            result.append(-1)

        for j in range(i+1, n):

            if(array[i] < array[j]):
                result.append(array[j])
                break
            
            if(j == (n-1)):
                result.append(-1)

    return result

def solve2(array):
    
    result = [-1] * n
    
    stack = [] 
    stack.append(0) 
    i = 1 
    
    while stack and i < n: 
        
        while stack and array[stack[-1]] < array[i]: 

            result[stack[-1]] = array[i] 
            stack.pop() 
            
        stack.append(i) 
        i += 1


    return result

    
result = solve2(array)

for x in result:
    print(x, end=' ')