T = int(input())
answer = 0
def recursion(s, l, r):
    global answer
    answer = answer + 1
    if l >= r :
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


for _ in range(T):
    strList = list(input())
    answer = 0
    print(recursion(strList, 0, len(strList)-1), end = " ")
    print(answer)
    