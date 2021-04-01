
n = int(input())
w = [0]

for i in range(n):
    w.append(int(input()))

d = [0]
d.append(w[1])

if(n>1):
    d.append(w[1]+w[2])

for i in range(3, n+1):
    d.append(max(d[i-1], d[i-3] + w[i-1] + w[i], d[i-2] + w[i]))


print(d[n])