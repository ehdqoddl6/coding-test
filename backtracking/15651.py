
import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(1, n+1):
    arr.append(str(i))

for x in list(product((arr), repeat=m)):
    for i in range(len(x)):
        print(x[i], end=' ')
    
    print()
