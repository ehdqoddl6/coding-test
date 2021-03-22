import sys

input = sys.stdin.readline

"""
n = int(input())
home_loc = list(map(int, input().split()))

"""
n = 4
home_loc = [5,1,7,9]

mid = int(n/2)-1


home_loc.sort()

first = 0
second = 0
for i in range(len(home_loc)):

    if(home_loc[i] <= home_loc[mid]):
        first = i
        break

for i in range(len(home_loc)):
    
    if(home_loc[i] >= home_loc[mid]):
        second = i
        break

sum1 = 0
sum2 = 0

for i in home_loc:

    sum1 += abs(i-home_loc[first])
    sum2 += abs(i-home_loc[second])

if(sum1 > sum2):
    print(home_loc[second])
else:
    print(home_loc[first])



