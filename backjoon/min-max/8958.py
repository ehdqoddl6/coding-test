n = int(input())

result_list = []


for i in range(n):
    result = input()
    result_list.append(result)


for result in result_list:
    i = 0
    sum = 0
    score = 0

    for i in range(len(result)):
        if(result[i] == 'O'):
            score += 1
            sum += score
        
        else:
            score = 0
            continue
    
    print(sum)

