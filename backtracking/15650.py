
import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n, m = map(int, input().split())


arr =[ i for i in range(1, n+1)]

for x in list(combinations(arr, m)):
    for i in range(len(x)):
        print(x[i], end=' ')
    
    print()
