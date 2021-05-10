def solution(code, day, data):
    answer = []
    
    temp = []
    for x in data:

        p, c, t = x.split(' ')
        
        a, price = p.split('=')
        a, cod = c.split('=')
        a, time = t.split('=')


        if(cod == code and time[0:8] == day):
            temp.append((price, int(time[8:])))

    
    temp = sorted(temp, key=lambda x:(x[1]))


    for x in temp:
        answer.append(int(x[0]))

    
    return answer


print(solution("012345", "20190620",	
["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014",
"price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009",
"price=95 code=012345 time=2019062111"]))