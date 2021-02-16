n = 5
moveList = ['R', 'R', 'R', 'R', 'U', 'D', 'D']

x = 1
y = 1
for move in moveList:
    print(x,y)
    #print(move)
    if(move == 'L'):
        print('L')
        if(y-1 > 1):
            y=y-1

    elif(move == 'R'):
        print('R')
        if(y+1<n):
            y=y+1
    
    elif(move == 'U'):
        print('U')
        if(x-1>1):
            x=x-1
    
    elif(move == 'D'):
        print('D')
        if(x+1<n):
            x=x+1

print(x,y)