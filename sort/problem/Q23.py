
import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    name, kok, eng, math = input().split()
    array.append((name, int(kok), int(eng), int(math)))

result = sorted(array, key=lambda x:(-x[1], x[2], -x[3], x[0]))   

print(result)

for x in result:
    print(x[0])
