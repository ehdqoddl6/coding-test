import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

"""
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

    if((mid == len(array)-1 or array[mid+1] > target) and array[mid] == target):
        return mid

    elif(array[mid] > target):
        return last(array, target, start, mid-1)

    else:
        return last(array, target, mid+1, end)

def solution(array, nums):
    result = []

    for x in nums:
        
        first_index = first(array, x, 0, len(array)-1)

        if(first_index == None):
            result.append(0)
            continue
        
        last_index = last(array, x, 0, len(array)-1)

        
        result.append(last_index - first_index + 1)

    return result

array.sort()
result = solution(array, nums)

for x in result:
    print(x, end=' ')
"""

array.sort()

def binary(array, target, start, end):

    if start > end:
        return 0

    mid = (start+end)//2
    if(array[mid] == target):
        return array[start:end+1].count(target)

    elif(array[mid] > target):
        return binary(array, target, start, mid-1)

    else:
        return binary(array, target, mid+1, end)

n_dic = {}
for x in array:
    
    if(x not in n_dic):
        n_dic[x] = binary(array, x, 0, len(array)-1)


for x in nums:

    if(x in n_dic):
        print(n_dic[x], end=' ')
    else:
        print(0, end=' ')
        