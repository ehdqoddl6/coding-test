

def fibo1(x):

    if(x == 1 or x == 2):
        return 1
    else:
        return fibo1(x-1) + fibo1(x-2)

#dynameic 에서는 불필요한 계산과정을 없앤다.
def fibo2(x):
    d = [0] * (x+1)

    d[1] = 1
    d[2] = 1

    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]
    
    return d[x]

print(fibo1(4))
print(fibo2(4))