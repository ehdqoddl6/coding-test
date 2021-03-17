
import sys

input = sys.stdin.readline

#input_data = input()



def solution(str1):

    num_list = []

    if(len(str1) == 1):
        return 1
        
    for i in range(1, len(str1)//2 + 1):

        #if(len(str1) % i == 0):
        num_list.append(i)

    print(num_list)

    str_list = []  
    for i in num_list:

          
        count = 0
        
        start = str1[0:i]

        #print(start)
        temp_str = ''
        for j in range(0, len(str1)+i, i):
            #print(j)
            #print(str1[j:j+i])
            if(start == str1[j:j+i]):
                count += 1
            else:
                if(count == 1):
                    temp_str += start
                else:
                    temp_str += str(count) + start
                
                start = str1[j:j+i]
                count = 1
        print(temp_str)
        str_list.append(int(len(temp_str)))
        #print(temp_str)
    print(str_list)
    return min(str_list)
#print(solution(input_data))
print(solution('a'))
