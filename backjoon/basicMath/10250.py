#num = int(input())


def solve(h, w, n):

    if(n % h == 0):
        floor = h
    else:
        floor = n % h

    
    ho = int((n-1) / h) + 1
    
    floor = str(floor)

    if(ho < 10):
        ho = '0' + str(ho)
    else:
        ho = str(ho)

    print(floor + ho)




"""
for i in range(num):
    h, w, n = map(int, input().split())

    solve(h, w, n)
"""
solve(30, 50, 72)