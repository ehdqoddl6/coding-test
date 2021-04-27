
from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])

cnt = 0
result = []
while(q):

    a = q.popleft()
    cnt += 1
    if(cnt % k == 0):
        result.append(a)
    
    else:
        q.append(a)

print('<', end='')
for i in range(len(result)):
    if(i != len(result)-1):
        print(result[i], end=', ')
    else:
        print(result[i], end='>')

