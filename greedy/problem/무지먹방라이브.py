

food_times = [3, 1, 2]
k =5


def solution(food_times, k):

    index = 0
    for i in range(k):
    
        if(sum(food_times) == 0):
            return -1

        if(index >= 3):
            index = index % 3

        if(food_times[index] != 0):
            food_times[index] -= 1
        
        else:
            
            while(True):
                index += 1

                if(index >= 3):
                    index = index % 3

                if(food_times[index] != 0):
                    food_times[index] -= 1
                    break


        index += 1

    return index%3 + 1




result = solution(food_times, k)
print(result)