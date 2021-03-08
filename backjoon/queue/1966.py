from collections import deque

k = int(input())


def solution(n, m, queue):

    index = deque([i for i in range(n)])
    result = []

    if(n == 1):
        return 1

    else:
        while(queue):
            
        
            if(queue[0] < max(queue)):
                a = queue.popleft()
                queue.append(a)

                a_index = index.popleft()
                index.append(a_index)

            else:
                queue.popleft()
                result.append(index.popleft())

            #print(queue, index, result)
            
        count = 1
        for x in result:
            
            if(x == m):
                return count
            else:
                count += 1


result = []
for i in range(k):

    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    #n = 6
    #m = 0
    #queue = deque([1,1,9,1,1,1])
    
    result.append(solution(n, m, queue))
    

for x in result:
    print(x)