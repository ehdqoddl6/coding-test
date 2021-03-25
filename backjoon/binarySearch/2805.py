"""
n, m = 4,7
array = [20,15,10,17]
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
"""
def binary(array, target, start, end):

    if(start > end):
        return None
    
    sum = 0
    mid = (start+end)//2

    for x in array:
        if(x > mid):
            sum += x-mid

    if(sum == target):
        return mid

    elif(sum > target):
        return binary(array, target, mid+1, end)
    
    else:
        return binary(array, target, start, mid-1)
"""

def solution(array, target, start, end):

    result = 0

    while(start <= end):

        sum = 0
        mid = (start + end)//2

        for x in array:
            if(x > mid):
                sum += (x-mid)

        if(sum < target):
            end = mid-1

        else:
            result = mid
            start = mid+1
    
    return result



print(solution(array, m, 0, max(array)))