#n, m = map(int, input().split())
#array = list(map(int, input().split()))

n = 5
m = 3

array = [1,3,2,3,2]
array = [1,5,4,3,2,4,5,2]
array = sorted(array)

count = 0

for i in range(len(array)-1):

    n = array[i]

    for j in range(i+1, len(array)):

        if(n < array[j]):
            count += 1


print(count)


