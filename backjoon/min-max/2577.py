
num_list = []

for i in range(3):
    num_list.append(int(input()))

prod = 1

for num in num_list:
    prod *= num


index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
index_count = [0,0,0,0,0,0,0,0,0,0]

prod = str(prod)

for i in prod:
    for j in index:

        if(i == j):
            index_count[int(j)] += 1
        

for i in index_count:
    print(i)