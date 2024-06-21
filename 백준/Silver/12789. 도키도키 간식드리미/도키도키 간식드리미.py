n = int(input())
stack = list(map(int, input().split()))
stack.reverse()
space = []
order = 1
while stack or space:
    if stack and stack[-1] == order:
        stack.pop()
        order += 1
    elif space and space[-1] == order:
        space.pop()
        order += 1
    else:
        if stack:
            space.append(stack.pop())
        else:
            break

if stack or space:
    print("Sad")
else:
    print("Nice")

    