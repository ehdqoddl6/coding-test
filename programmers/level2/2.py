def solution(record):
    answer = []
    
    ID = []
    name = []

    for i in range(len(record)):

        user = record[i].split()
        
        if(len(user) == 3):

            if(user[1] not in ID):
                ID.append(user[1])
                name.append(user[2])
            else:
                index = ID.index(user[1])
                name[index] = user[2]

    for i in range(len(record)): 

        user = record[i].split()
        
        if(len(user) == 3):

            if(user[0] == 'Enter'):
                index = ID.index(user[1])
                answer.append("{}님이 들어왔습니다.".format(name[index]))

        else:

            index = ID.index(user[1])
            answer.append("{}님이 나갔습니다.".format(name[index]))


    return answer



a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(a))