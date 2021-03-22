

n = 2

stages = [1,2,1,3]



def solution(N, stages):

    answer = []
    fail = []

    stages.sort()

    for i in range(1, N+1):
        fail_num = 0
        suc_num = 0

        for j in stages:
            if(i == j):
                fail_num += 1
            
            elif(j > i):
                suc_num += 1
        
        tot_num = fail_num + suc_num
        ui
        if(tot_num == 0):
            fail.append((i, 0))
        else:
            fail.append((i, fail_num/tot_num))

    result = sorted(fail, key=lambda x:(-x[1]))   
    
    
    for i in result:
        answer.append(i[0])
    
    
    return answer


print(solution(n, stages))