a, b, c = map(int, input().split())

value1 = (a+b)%c
value2 = ((a%c)+(b%c))%c

value3 = (a*b)%c
value4 = ((a%c)*(b%c))%c

print(value1)
print(value2)
print(value3)
print(value4)



