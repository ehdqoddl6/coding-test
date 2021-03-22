import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

max = -1

for i in nums:
    sum = 0
    sum += i
    #print('frist : ', i)

    for j in nums:

        if(j != i):
            temp_sum = sum + j

            #print('second : ', j)
            for k in nums:
                
                if(k != i and k != j):
                    #print('thrid : ', k)
                    if((temp_sum + k) <= m and (temp_sum+k) > max):
                        
                        max = temp_sum + k
                        #print(i, j, k, max)


print(max)