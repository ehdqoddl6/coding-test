def solve(a,b,c):
    if((a*a + b*b) == (c*c) or (a*a + c*c) == (b*b) or (c*c + b*b) == (a*a)):
        return 'right'
    
    else:
        return 'wrong'

answer = []
while(True):
    a, b, c = map(int, input().split())

    if(a == 0):
        break

    answer.append(solve(a,b,c))

for i in answer:
    print(i)