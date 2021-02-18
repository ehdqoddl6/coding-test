
num_list = []

for i in range(9):
    num_list.append(int(input()))

max_value = max(num_list)

index = 1

for num in num_list:
    if(num == max_value):
        break
    else:
        index += 1

print(max_value)
print(index)