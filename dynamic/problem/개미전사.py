n = int(input())

array = list(map(int, input().split()))

store = [0] * n

store[0] = array[0]
store[1] = max(array[0], array[1])

for i in range(2, n):
    store[i] = max(store[i-1], store[i-2]+array[i])

    print(store)


print(store[n-1])