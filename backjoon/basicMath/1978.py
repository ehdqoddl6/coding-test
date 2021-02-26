
n = int(input())
num_list = list(map(int, input().split()))

#print(num_list)

def solve(num):

    if(num == 1):
        return False

    for i in range(2, num):

        if(num % i == 0):
            return False

    return True
        

count = 0
for i in num_list:
    if(solve(i)):
        count += 1


print(count)