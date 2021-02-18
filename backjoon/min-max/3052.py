
num_list = []

for i in range(10):
    num_list.append(int(input()))

mod_list = []

for num in num_list:
    mod_list.append(num%42)

uni_list = []

for num in mod_list:
    if(num not in uni_list):
        uni_list.append(num)
    



print(len(uni_list))
