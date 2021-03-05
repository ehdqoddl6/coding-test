#큰수의 법칙
n = 5
m = 8
k = 3
num = [2, 4, 5, 4, 6]

sum = 0

num = sorted(num)

print(num)
count = 0
index = len(num) - 1
value = num[index]
a = 0

for i in range(0, m):
    
    count += 1
    
    if(count % (k+1) != 0):
        
        sum = sum + value
        print(sum)
        
    else:

        sum = sum + num[index-1]
        print(sum)
        """
        a += 1
        if(a % 2 == 1):
            value = num[index-1]
        else:
            value = num[index]

        sum = sum + value
        print(sum)
        """
        
print(sum)