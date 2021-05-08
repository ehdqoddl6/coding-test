def solution(s):

    answer = ''
    temp_str = ''

    for i in range(len(s)):
        if(s[i] >= '0' and s[i] <= '9'):
            answer += s[i]
        
        else:
            temp_str += s[i]

            if(temp_str == 'one'):
                answer += '1'
                temp_str = ''
            
            elif(temp_str == 'zero'):
                answer += '0'
                temp_str = ''

            elif(temp_str == 'two'):
                answer += '2'
                temp_str = ''
            
            elif(temp_str == 'three'):
                answer += '3'
                temp_str = ''
            
            elif(temp_str == 'four'):
                answer += '4'
                temp_str = ''
            
            elif(temp_str == 'five'):
                answer += '5'
                temp_str = ''
            
            elif(temp_str == 'six'):
                answer += '6'
                temp_str = ''
            
            elif(temp_str == 'seven'):
                answer += '7'
                temp_str = ''
            
            elif(temp_str == 'eight'):
                answer += '8'
                temp_str = ''
            
            elif(temp_str == 'nine'):
                answer += '9'
                temp_str = ''



    return int(answer)

