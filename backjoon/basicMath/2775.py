
#num = int(input())


def solve(k, n):

    n_list = [i for i in range(1, 15)]

    last_list = []

    for i in range(k):
        ho_sum = []
        sum = 0
        if(i == 0):
            for j in range(n):
                sum = sum + n_list[j]
                ho_sum.append(sum)
                
        else:
            for j in range(n):
                sum = sum + last_list[j]
                ho_sum.append(sum)
                


        last_list = ho_sum
        

    print(last_list[n-1])



"""
for i in range(num):
    k = int(input())
    n = int(input())

    solve(k, n)
"""

solve(2, 3)