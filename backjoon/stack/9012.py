
n = int(input())

result = []
for i in range(n):

    count = 0


    str = input()

    for i in str:

        if(i == '('):
            count += 1
        else:
            count -= 1
        
        if(count < 0):
            break


    if(count == 0):
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)
