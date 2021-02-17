a = input()
b = input()


alen = len(a)
blen = len(b)

a = int(a)

value_list = []
c = 1

for i in range(blen-1, -1, -1):
    value_list.append(a*int(b[i])*c)
    c = c * 10

sum = 0

c = 1
for value in value_list:
    print(int(value / c))
    c = c * 10
    sum += value

print(sum)