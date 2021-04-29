
import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

"""
arr = []
for i in range(1, n+1):
    arr.append(str(i))
"""
arr =[ i for i in range(1, n+1)]
for x in list(combinations_with_replacement(arr, m)):
    for i in range(len(x)):
        print(x[i], end=' ')
    
    print()
