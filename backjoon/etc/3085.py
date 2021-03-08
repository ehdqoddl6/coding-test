n = int(input())

color = []
for i in range(n):
    color.append(input())

def getMaxLen(str, n):
    
    count = 1
    start = str[0]
    max_count = 1

    for i in range(1, n):
        
        if(start == str[i]):
            count += 1
            start = str[i]

        else:
            count = 1
            start = str[i]

        if(max_count < count):
            max_count = count

    return max_count

def getMax(color, n, maxLen):

    for i in range(n):
        result = getMaxLen(color[i], n)
        if(maxLen < result):
            maxLen = result

    for i in range(n):
        
        str1 = ''
        for j in range(n):
            
            str1 = str1 + color[j][i]
        
        
        result = getMaxLen(str1, n)
        if(maxLen < result):
            maxLen = result

    return maxLen

def side_switching(color, i, j):


    #print(color[i][j], color[i][j+1])
    """
    temp = color[i][j]
    color[i] = color[i].replace(color[i][j], color[i][j+1], 1)
    color[i] = color[i].replace(color[i][j+1], temp, 1)
    """
    a = list(color[i])
    a[j], a[j+1] = a[j+1], a[j]

    color[i] = a

    #print(color[i][j], color[i][j+1])
    #print(color)

    return color

def down_switching(color, i, j):

    #print(color[i][j], color[i+1][j])
    """
    temp = color[i][j]
    color[i] = color[i].replace(color[i][j], color[i+1][j], 1)
    color[i+1] = color[i+1].replace(color[i+1][j], temp, 1)
    """
    a = list(color[i])
    b = list(color[i+1])

    a[j], b[j] = b[j], a[j]

    color[i] = a
    color[i+1] = b

    #print(color[i][j], color[i+1][j])
    #print(color)
    return color

def solution(color, n):

    maxLen = 0

    maxLen = getMax(color, n, maxLen)
    
            
    for i in range(n):
        for j in range(n):
            
            if(i==0):
                if(j != n-1):

                    color = side_switching(color, i, j)
                    maxLen = getMax(color, n, maxLen)
                    color = side_switching(color, i, j)
                   
                    color = down_switching(color, i, j)
                    maxLen = getMax(color, n, maxLen)
                    color = down_switching(color, i, j)

                else:
                    color = down_switching(color, i, j)
                    maxLen = getMax(color, n, maxLen)
                    color = down_switching(color, i, j)

            elif(i==n-1):
                if(j != n-1):
                    color = side_switching(color, i, j)
                    maxLen = getMax(color, n, maxLen)
                    color = side_switching(color, i, j)

            else:
                if(j != n-1):
                    color = side_switching(color, i, j)
                    maxLen = getMax(color, n, maxLen)
                    color = side_switching(color, i, j)
                   
                    color = down_switching(color, i, j)
                    maxLen = getMax(color, n, maxLen)
                    color = down_switching(color, i, j)


                else:
                    color = down_switching(color, i, j)
                    maxLen = getMax(color, n, maxLen)
                    color = down_switching(color, i, j)

    print(maxLen)


solution(color, n)



