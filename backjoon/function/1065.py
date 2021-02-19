def solve(num):

    count = 0
    for i in range(1, num+1):

        num_str = str(i)

        
        if(len(num_str) <= 2):
            count += 1
            

        else:
            prod = 25252525
            for j in range(len(num_str)-1):
    
                if(j == 0):
                    if(int(num_str[j] != 0)):
                        prod = int(num_str[j+1]) - int(num_str[j])
                    
                    else:
                        break

                else: 
                
                    if(int(num_str[j]) != 0):

                        if(j != len(num_str)-2):
                            if(int(num_str[j+1])-int(num_str[j]) == prod):
                                continue
                        
                        else:
                            if(int(num_str[j+1])-int(num_str[j]) == prod):
                                count += 1
                                
                                
                        
                    else:
                        break

            
    
        
    print(count)
        



num = int(input())

solve(num)