import sys

input = sys.stdin.readline


n = int(input())
array = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

def binary(array, target, start, end):

    if(start > end):
        return 0

    mid = (start+end)//2

    if(array[mid] == target):
        return 1
    
    elif(array[mid] > target):
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)


    


def solution(array, nums):

    result = []

    for i in nums:
        result.append(binary(array, i, 0, len(array)-1))

    return result

array.sort()
result = solution(array, nums)

for x in result:
    print(x)