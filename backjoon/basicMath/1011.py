#n = int(input())

def solve(x,y):
    
    distance = y - x 

    count = 0
    move = 1
    move_plus = 0

    while(move_plus < distance):
        print('a', move)
        count += 1

        move_plus += move
        if(count % 2 == 0):
            move += 1
    
    print(count)





"""
for i in range(n):
    x, y = map(int, input().split())

    solve(x, y)
"""

solve(0, 3)
solve(1, 5)
solve(45, 50)