
import sys

input = sys.stdin.readline

"""
n, target = map(int, input().split())
array = list(map(int, input().split()))
"""

n, target = 7, 2
array = [1,1,2,2,2,2,3]

def first(array, target, start, end):

    if(start > end):
        return None

    mid = (start+end)//2

    if((mid == 0 or array[mid-1] < target) and array[mid] == target):
        return mid
    
    elif(array[mid] >= target):
        return first(array, target, start, mid-1)

    else:
        return first(array, target, mid+1, end)

def last(array, target, start, end):

    if(start > end):
        return None

    mid = (start+end)//2

    if((mid == n-1 or array[mid+1] > target) and array[mid] == target):
        return mid
    
    elif(array[mid] > target):
        return last(array, target, start, mid-1)

    else:
        return last(array, target, mid+1, end)


def solution(array, target):

    n = len(array)    
    first_index = first(array, target, 0, n-1)

    print(first_index)
    if(first_index == None):
        return 0

    last_index = last(array, target, 0, n-1)

    return last_index - first_index + 1


result = solution(array, target)

if(result == 0):
    print(-1)

else:
    print(result)
