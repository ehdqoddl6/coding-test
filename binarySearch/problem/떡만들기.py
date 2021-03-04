#n, m = map(int, input().split())
#duk_list = list(map(int, input().split()))

n, m = 4,6
duk_list = [19,15,10,17]


def binary_search(array, target, start, end):

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



result = binary_search(duk_list, m, 0, max(duk_list))
print(result)

