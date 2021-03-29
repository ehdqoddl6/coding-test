
n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
"""
n = 5
dist = [3,2,1,4]
price = [5,8,9,4,1]
"""
def solution(dist, price):

    cost = 0
    """
    if(min(price) == price[0]):
        return sum(dist)*price[0]

    else:
        for i in range(1, len(price)):
            if(price[0] > price[i]):
                break

        dis_sum = 0
        for x in range(i):
            dis_sum += dist[x]

        cost = dis_sum * price[0]
    return cost + solution(dist[i:], price[i:])
    """
    """
    i = 0
    while(True):

        if(min(price) == price[i]):
            
            a = 0
            #for x in range(i, n-1):
                #a += dist[x]
             
            a = sum(dist[i:n-1])
            cost += a*price[i]
            break

        else:
            
            for j in range(i+1, n-1):
                if(price[i] > price[j]):
                    break
            
            a = 0
            for x in range(i, j):
                a += dist[x]
            
            a = sum(dist[i:j])
            cost += a * price[i]

            i = j
    """
    """
    while(True):

        if(len(dist) == 0):
            break

        min_value = min(price)
        min_index = price.index(min_value)

        cost += sum(dist[min_index:])*min_value

        dist = dist[0:min_index]
        price = price[0:min_index]

"""
    cost = dist[0] * price[0]
    cur_price = price[0]
    cur_dist = 0
    for i in range(1, n-1):
        if(price[i] < cur_price):
            cost += cur_price*cur_dist
            cur_dist = dist[i]
            cur_price = price[i]
        else:
            cur_dist += dist[i]

        if(i == n-2):
            cost += cur_price*cur_dist

             
    return cost

print(solution(dist, price[0:n-1]))