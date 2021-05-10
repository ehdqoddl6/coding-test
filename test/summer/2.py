import heapq


def solution(t, r):
    answer = []
    arr = []
    q = []
    for i in range(len(t)):
        arr.append((r[i], t[i], i))
    
    


    time = 0
    
    while(arr):

        for x in arr:
            if(x[1] == time):
                heapq.heappush(q, x)

        q = sorted(q, key=lambda x:(x[0], x[2]))
        heapq.heapify(q)

        if(len(q) >= 1):
            data = heapq.heappop(q)
            idx = arr.index(data)
            arr.pop(idx)
            answer.append(data[2])

        time += 1

            
    return answer


print(solution([0,1,3,0], [0,1,2,3]))