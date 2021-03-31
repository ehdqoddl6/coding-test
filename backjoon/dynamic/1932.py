
n = int(input())


nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

for i in range(n-1):

    for j in range(len(nums[i])):

        if(j==0):
            nums[i+1][j] = max(nums[i+1][j], nums[i+1][j]+nums[i][j])
            nums[i+1][j+1] = max(nums[i+1][j+1], nums[i+1][j+1]+nums[i][j])

        else:
            nums[i+1][j] = max(nums[i+1][j], nums[i+1][j]-nums[i][j-1]+nums[i][j])
            nums[i+1][j+1] = max(nums[i+1][j+1], nums[i+1][j+1]+nums[i][j])


print(max(nums[n-1]))