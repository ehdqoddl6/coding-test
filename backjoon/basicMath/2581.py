n = int(input())
m = int(input())

num_list = [i for i in range(n, m+1)]

def solve(num):

    if(num == 1):
        return False

    for i in range(2, num):

        if(num % i == 0):
            return False

    return True
        

prime_list = []
for i in num_list:
    if(solve(i)):
        prime_list.append(i)

if(len(prime_list) == 0):
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))