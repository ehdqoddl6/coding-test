

input_value = "c2"

print(input_value)

x_list = ['a', 'b', 'c', 'd', 'e','f','g','h']

x = 0
y = int(input_value[1])

for i in x_list:
    x += 1
    if(input_value[0] == i):
        break

print(x,y)

count = 0    

move_list = [
    [-2, -1],
    [-2, 1],
    [-1, -2],
    [-1, 2],
    [2, -1],
    [2, 1],
    [1, -2],
    [1, 2]
]

for i in move_list:
    if(x + int(i[0]) < 1 or y + int(i[1]) < 1 or x + int(i[0]) > 8 or y + int(i[1]) > 8):
        continue
    else:
        count +=1

print(count)