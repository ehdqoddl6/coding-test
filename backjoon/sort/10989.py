import sys

n = int(sys.stdin.readline())

freq = [0] * 10001
for i in range(n):
    num = int(sys.stdin.readline())
    freq[num] += 1

for i in range(len(freq)):
    for j in range(freq[i]):
        print(i)


