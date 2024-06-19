# ( -> 스택에 넣고 ) -> 스택에서 pop !
n = int(input())

for i in range(n):
    vps = input()
    vpsList = list(vps) # list로 만들기
    stack = []
    result = True
    for j in vpsList:
        if j == '(': # ( 일 경우
            stack.append(j)
        else:   # ) 일 경우
            if len(stack) == 0: # 스택이 비어있다면
                print("NO")
                result = False
                break
            else:
                stack.pop()
    if len(stack) == 0:
        if result == True:
            print("YES")
    else:
        if result == True:
            print("NO")
