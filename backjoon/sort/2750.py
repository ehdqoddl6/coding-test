
n = int(input())

num = []
for i in range(n):
    a = int(input())
    num.append(a)


def solution(array):

    for i in range(len(array)):
        min_index = i

        for j in range(i+1, len(array)):
            if(array[min_index] > array[j]):
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]

    return array
        

num = solution(num)

for x in num:
    print(x)