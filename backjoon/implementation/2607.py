import sys

input = sys.stdin.readline

n = int(input())
compare = list(input())
ans = 0

for _ in range(n-1):
    compare_word = compare[:]
    check_word = list(input())

    for _ in range(len(check_word)):
        a = check_word.pop(0)
        if(a in compare_word):
            compare_word.remove(a)
        else:
            check_word.append(a)
    
    A = len(compare_word)
    B = len(check_word)

    if(A == 0 and B==0) or (A == 1 and B==0) or (A==0 and B==1) or (A == 1 and B==1):
        ans += 1

print(ans)