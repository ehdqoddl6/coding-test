
n = int(input())
item_list = list(map(int, input().split()))

m = int(input())
req_list = list(map(int, input().split()))

item_list.sort()


def binary_search(array, i, start, end):

    if(start > end):
        return 'no'
    
    mid = (start + end)//2

    if(array[mid] == i):
        return 'yes'

    elif(array[mid] > i):
        return binary_search(array, i, 0, mid-1)
        
    else:
        return binary_search(array, i, mid+1, end)

for i in req_list:
    result = binary_search(item_list, i, 0, len(item_list)-1)
    print(result, end=' ')