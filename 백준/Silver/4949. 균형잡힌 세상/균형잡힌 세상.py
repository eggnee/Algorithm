import sys

while True:
    cmd = list(sys.stdin.readline().rstrip())
    if cmd[0] == '.':
        break
    stack = []
    for i in cmd:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                print("no")
                break
        elif i == ']':
            if not stack or stack.pop() != '[':
                print("no")
                break
        elif i == '.':
            if stack:
                print("no")
            else:
                print("yes")
    