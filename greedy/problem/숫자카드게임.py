n = 2
m = 4
num = [
    [3,1,2],
    [4,1,4],
    [2,2,2]
]

num = [
    [7,3,1,8],
    [3,3,3,4]
]

cho_num = []
for i in range(0,n):
    value = min(num[i])
    cho_num.append(value)

print(max(cho_num))


