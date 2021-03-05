
n = input()

count0 = 0
count1 = 0

if(n[0] == '1'):
    count0 += 1
else:
    count1 += 1

for i in range(len(n)-1):

    if(n[i] != n[i+1]):

        if(n[i+1] == '1'):
            count0 += 1
        else:
            count1 += 1

print(count0, count1)