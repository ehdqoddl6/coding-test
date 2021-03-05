#n =  int(input())

#hu_list = list(map(int, input().split()))

hu_list = [1,2,3,4,5]
print(hu_list)


hu_list = sorted(hu_list)

a = 1
i = 0
count = 0
while(True):
    #print(i)
    if(i == len(hu_list)-1 or hu_list[i] > len(hu_list[i:])):
        break

    num = hu_list[i]

    for j in range(num):
        j += 1

        if(j == num):
            count += 1
            i = i+j

print(count)

count = 0
result = 0
for i in hu_list:
    count += 1

    if(count >= i):
        result += 1
        count = 0

print(result)

