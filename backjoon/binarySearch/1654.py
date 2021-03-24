

n, k = map(int, input().split())

array = []

for _ in range(n):
    array.append(int(input()))

"""
n, k = 4,11
array = [802,743,457,539]
"""

array.sort()
start, end = 1, max(array)

while(start <= end):

    mid = (start + end) // 2

    line = 0

    for i in array:
        line += i//mid

    if(line >= k):
        start = mid + 1
    
    else:
        end = mid - 1

    

print(end)
