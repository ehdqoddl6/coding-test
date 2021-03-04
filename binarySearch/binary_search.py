array = [1,3,5,7,9,11,13,15,17,19]

def binary_search(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end)//2

    if(array[mid] == target):
        return mid
    
    elif(array[mid] > target):
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)

print(binary_search(array, 7, 0, len(array)-1))