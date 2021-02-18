n = int(input())



num_list = list(map(int, input().split()))

num_list = num_list[0:n]

print(min(num_list), max(num_list))