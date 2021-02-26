import math

def solve(num):
    
    if(num == 1):
        return False

    
    for i in range(2,int(math.sqrt(num)+1)):

        if(num % i == 0):
            return False

    return True

count_list = []

li = list(range(2,246912))
prime_li = []
for i in li:
    if solve(i):
        prime_li.append(i)

while(True):
    n = int(input())

    if(n == 0):
        break

    

    count = 0
    for i in prime_li:
        if n < i <= n*2:
            count += 1

    count_list.append(count)

        

for i in count_list:
    print(i)