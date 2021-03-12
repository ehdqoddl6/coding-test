
n = int(input())


def solution(loc):
    
    dis = []
    for i in range(len(loc)-1):
        sum = 0
        for j in range(len(loc[i])):

            sum += abs((loc[i][j] - loc[i+1][j]))
        dis.append(sum)

    for x in dis:
        if(x > 1000):
            return "sad"
    
    return "happy"

result = []
for i in range(n):
    loc = []
    con = int(input())
    a, b = map(int, input().split())
    loc.append([a, b])

    for j in range(con):
        a, b = map(int, input().split())

        loc.append([a, b])

    a, b = map(int, input().split())
    loc.append([a, b])
    
    result.append(solution(loc))


for x in result:
    print(x)
