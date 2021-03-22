
n, m = map(int, input().split())

ches = []
for i in range(n):
    ches.append(input())

def edit_count(ches):
    count1 = 0
    count2 = 0

    
    for i in range(8):

        for j in range(8):
            
            if((i+j)%2 == 0):
                if(ches[i][j] != 'W'):
                    count1 += 1
                if(ches[i][j] != 'B'):
                    count2 += 1
            
            else:
                if(ches[i][j] != 'B'):
                    count1 += 1
                if(ches[i][j] != 'W'):
                    count2 += 1
           
                       


    return min(count1, count2)

def solution(ches):

    min = 1e10
    result = []
    num_col = m - 7
    num_ver = n - 7

    for i in range(num_col):
        temp_ches = []

        for x in ches:
            temp_ches.append(x[i:i+8])
        
        #print(temp_ches)
        for x in range(num_ver):
            result = edit_count(temp_ches[x:x+8])

            if(result < min):
                min = result

    return min

print(solution(ches))