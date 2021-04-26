
n = int(input())
arr = []

for _ in range(n):
    w, h = map(int, input().split())
    arr.append((w,h))



for i in arr:
    rank = 1

    for n in arr:
        if((i[0] < n[0]) and (i[1] < n[1])):
            rank += 1
    

    print(rank)