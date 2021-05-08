
def solution(n, k, cmd):
    answer = ''
    
    cur_state = ['O'] * n
    del_index = []
    cur_index = k
    m = [i for i in range(n)]

    for x in cmd:
        #print(cur_index, cur_state)
        if(len(x) != 1):
            exe, i = x.split(' ')
            i = int(i)

            if(exe == 'D'):
    
                d = 0
                cnt = 0
                for q in range(cur_index+1, n):
                    if(q in del_index):
                        d += 1
                    else:
                        if(cnt != i):
                            d+=1
                            cnt += 1

                            if(cnt == i):
                                break
                        


                cur_index = cur_index + d
         
            elif(exe == 'U'):

                d = 0
                cnt = 0
                for q in range(cur_index-1, -1, -1):
                    if(q in del_index):
                        d += 1
                    else:
                        if(cnt != i):
                            d+=1
                            cnt += 1
                            if(cnt == i):
                                break
            
                cur_index = cur_index - d

        else:
            exe = x
        
            if(exe == 'C'):
                cur_state[cur_index] = 'X'
                com = list(set(m)-set(del_index))
                del_index.append(cur_index)

                
                #print(cur_index, max(com))
                if(cur_index == max(com)):
                    
                    a = 0
                    for t in range(cur_index-1, -1, -1):
                        
                        if(t in del_index):
                            a += 1
                        else:
                            break

                    cur_index = cur_index - a - 1

                else:
                    a = 0
                    for t in range(cur_index+1, n):
                        
                        if(t in del_index):
                            a += 1
                        else:
                            break

                    cur_index = cur_index + a+1
            
            
            elif(exe == 'Z'):
                idx = del_index.pop()
                cur_state[idx] = 'O'

                

        #print(cur_index, cur_state)
        
        
    for i in cur_state:
        answer += i

    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))