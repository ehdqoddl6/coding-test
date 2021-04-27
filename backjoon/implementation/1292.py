
a, b = map(int, input().split())

cnt = 0
value = 1
nums = []

while(cnt < b):

    for i in range(value):
        nums.append(value)
        cnt += 1
    
    value += 1
    

print(sum(nums[a-1:b]))