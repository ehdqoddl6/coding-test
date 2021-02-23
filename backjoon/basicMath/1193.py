
x = int(input())

if(x == 1):
    print('1/1')

else:

    num = 1
    sum = 0

    while(True):

        if(x <= sum):
            break
        else:
            sum += num
            num += 1

    i=0
    j=0

    if((num - 1) % 2 == 1):
    
        i = num - 1
        j = 1
        
        for k in range(sum-num+2, x):
            i -= 1
            j += 1

    else:
        i = 1
        j = num - 1

        for k in range(sum-num+2, x):
            i += 1
            j -= 1

    print('{}/{}'.format(i,j))       
