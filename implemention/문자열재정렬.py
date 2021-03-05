#input_data = input()

def solution(data):

    str_list = []
    num_list = []

    for i in range(len(data)):

        if(data[i] >= '0' and data[i] <= '9'):
            num_list.append(int(data[i]))
        
        else:
            str_list.append(data[i])
    
    str_list.sort()
    result = ''

    for x in str_list:
        result += x
    
    
    result += str(sum(num_list))
    
    return result



print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ9D'))
#print(solution(input_data))