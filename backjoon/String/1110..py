

n = input()



temp_n = n
count = 0

result = 0

if(n == '0'):
    print(1)

else:
    while(int(n) != int(result)):

        digit_sum = 0

        for x in temp_n:
            digit_sum += int(x)
        
        result = temp_n[-1] + str(digit_sum)[-1]

        temp_n = result
        count += 1

    print(count)