array = input()
tmp = 1
answer = 0
stack = []

for i in range(len(array)):
    if array[i] == "(":
        stack.append(array[i])
        tmp = tmp * 2
    elif array[i] == "[":
        stack.append(array[i])
        tmp = tmp * 3
    elif array[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if array[i-1] == "(":
            answer = answer + tmp
        stack.pop()
        tmp = tmp // 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if array[i-1] == "[":
            answer = answer + tmp
        stack.pop()
        tmp = tmp // 3

if stack:
    print(0)
else:
    print(answer)
        