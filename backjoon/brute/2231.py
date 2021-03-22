
n = int(input())

def solution(n):

    for i in range(1, n+1):
        
        num = i
        num_str = str(num)
        
        sum = 0
        for x in num_str:
            sum += int(x)
        
        if(num + sum == n):
            return num
        
    return 0

print(solution(n))
