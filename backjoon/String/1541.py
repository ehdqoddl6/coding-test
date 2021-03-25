


#a = input()
a = '10+10-10+10-10+10-10+10'
#a = '55-50+40'
sum = 0

temp_num = ''
cal = []
nums = []

for x in a:
    
    if(x >= '0' and x <= '9'):
        temp_num += x
    
    else:
        nums.append(int(temp_num))
        cal.append(x)
        temp_num = ''

nums.append(int(temp_num))

if(len(cal) == 0):
    print(nums[0])

else:
    sum = nums[0]
    nums = nums[1:]

    #index1 = 0
    #j = 0
    print(cal)
    for i in range(len(cal)):
        
        print('i = ',i)
        if(cal[i] == '-'):
            #print(cal[i+1:])

            if('-' in cal[i+1:]):
                index1 = i + cal[i+1:].index('-')

                for j in range(i+1, index1+1):
                    print(j)
                    cal[j] = '-'
                
                i = index1
            
            

    index = 0
    for i in range(len(cal)):
        
        if(cal[i] == '-'):
            index = i


    if(index != 0):
        for i in range(index+1, len(cal)):
            cal[i] = '-'


    print(cal)

    for i in range(len(nums)):
        if(cal[i] == '+'):
            sum += nums[i]
        else:
            sum -= nums[i]

    print(sum)