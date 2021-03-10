
import sys

n = int(sys.stdin.readline())

num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))



num.sort()


print(round(sum(num)/n))
print(num[n//2])


def find_frequency(array):

    min_value = min(array)

    if(len(array) == 1):
        return array[0]

    if(min_value < 0):
        
        for i in range(len(array)):
            array[i] = array[i] - min_value


    freq = [0] * (max(array)+1)

    for i in array:
        freq[i] += 1

    a = []

    for i in range(len(freq)):
        if(max(freq) == freq[i]):
            a.append(i)
    
    if(min_value < 0):
        
        if(len(a) == 1):
            return a[0] + min_value

        else:
            return a[1] + min_value
    else:
        if(len(a) == 1):
            return a[0] 

        else:
            return a[1]

print(find_frequency(num))

if(len(num) == 1):
    print(0)
else:
    print(num[-1] - num[0])

