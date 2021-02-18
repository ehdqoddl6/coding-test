
num = int(input())

a = []
b = []

for i in range(0, num):
    num1, num2 = map(int, input().split())

    a.append(num1)
    b.append(num2)

for i in range(0, num):

    print('Case #{}: {} + {} = {}'.format(i+1, a[i], b[i], int(a[i]) + int(b[i])))