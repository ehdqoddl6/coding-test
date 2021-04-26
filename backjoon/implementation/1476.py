
e, s, m = map(int, input().split())

a, b, c = 1, 1, 1

count = 1

while(True):

    if(e == a and s == b and m == c):
        break
    
    a += 1
    b += 1
    c += 1

    if(a > 15):
        a -= 15
    if(b > 28):
        b -= 28
    if(c > 19):
        c -= 19

    count += 1

print(count)