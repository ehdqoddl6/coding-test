n, k = map(int, input().split())


nums = [i for i in range(2, n+1)]
cnt = 0
while(cnt < k):

    min_value = min(nums)

    for j in nums:

        if(j % min_value == 0):
            idx = nums.index(j)
            result = nums.pop(idx)
            cnt += 1
            
            if(cnt == k):
                print(result)

           
