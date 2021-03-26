k = int(input())
t = 2**k - 1
res = t*(t+1)//2
print(res)
print(bin(res)[2:])

"""
2진수 변환 : bin()
8진수 변환 : oct()
16진수 변환 : hex()
"""
