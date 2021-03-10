n = int(input())

num = []
for i in range(n):
    num.append(int(input()))


def solution(array):

    if(len(array) <= 1):
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return solution(left_side) + [pivot] + solution(right_side)

num = solution(num)

for x in num:
    print(x)

