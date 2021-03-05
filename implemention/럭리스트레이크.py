
input_data = input()

def solution(data):

    mid = len(data) // 2

    str1 = data[0:mid]
    str2 = data[mid:]
    print(str1, str2)
    sum1 = 0
    sum2 = 0

    for i in range(len(str1)):

        sum1 += int(str1[i])
        sum2 += int(str2[i])

    
    print(sum1, sum2)
    if(sum1 == sum2):
        return 'LUCKY'

    else:
        return 'READY'

        
print(solution(input_data))
