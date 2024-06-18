import sys

k = int(input())
stack = []
for i in range(k):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))