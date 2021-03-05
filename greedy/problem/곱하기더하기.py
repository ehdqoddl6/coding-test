

n = input()

sum = 0


for i in range(len(n)):

    b = int(n[i])

    if(sum == 0 or sum == 1 or b == 0 or b == 1):
        sum = sum + b

    else:
        sum = sum * b 


print(sum)

