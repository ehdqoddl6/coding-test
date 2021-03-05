#처음 생각한 것
#k로 계속 나누고 k보다 작을때 1씩 뺄때 최적의 해 구할 수 있다고 생각함
#하지만, 나누어 떨어지지 않는 경우를 생각하지 않음.



n = 25
k = 5


count = 0

while(n != 1):
    print(n)

    if(n >= k and n % k == 0):
        n = n / k
        count += 1

    elif(n >= k and n % k != 0):
        n = n-1
        count +=1

    elif(n < k):
        n = n - 1
        count+=1

print(count)
