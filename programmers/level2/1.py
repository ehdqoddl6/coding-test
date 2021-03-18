def solution(s):
    answer = 0

    str_data = s
    
    while(True):
        
        start = str_data[0]
        count = 1
        
        flag = False
        for i in range(1, len(str_data)):
            
            if(start == str_data[i]):
                count += 1
            else:
                start = str_data[i]
                count = 1
            
            if(count == 2):
                flag = True
                if(i < 2):
                    temp_str = str_data[i+1:]
                    str_data = temp_str

                else:
                    temp_str = str_data[0:i-1] + str_data[i+1:]
                    str_data = temp_str
                
                break

        if(flag == False or len(str_data) == 0):
            break
    
    if(len(str_data) == 0):
        answer = 1


    return answer

print(solution('cdcd'))