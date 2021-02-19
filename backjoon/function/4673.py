def solve():
    
    
    num_list = []

    for num in range(1, 10001):
        sum = 0

        sum += num
        num_str = str(num)
        
        for i in num_str:
            sum += int(i)

        num_list.append(sum)
        
    
    
    for i in range(1, 10001):
        if(int(i) not in num_list):
            print(i)
            
        
        
solve()

