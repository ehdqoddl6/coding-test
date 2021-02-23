h, m = map(int, input().split())

#h, m = 0, 30

if(m >= 45):
    print(h, m-45)
else(m < 45):
    if(h > 0):
        print(h-1, m+15)
    else:
        print(23, m+15)