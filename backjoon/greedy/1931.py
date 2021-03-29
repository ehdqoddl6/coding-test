
n = int(input())

nums = list(map(int, input().split()))

nums.sort()

sum1 = 0

delay = []
for x in nums:

    sum1 = sum1 + x
    delay.append(sum1)


print(sum(delay))