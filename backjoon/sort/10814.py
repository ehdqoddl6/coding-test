import sys

n = int(sys.stdin.readline())

info = []

for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    info.append((int(age), name, i))

# - 붙이면 내림차순!
info.sort(key=lambda x:(x[0], x[2])) 

for x in info:
    print(x[0], x[1])