N = int(input())
answer = 0

for _ in range(N):
    stack = []
    word = input()
    for w in word:
        if stack:
            if stack[-1] == w:
                stack.pop()
                continue
        stack.append(w)
    if not stack:
        answer += 1
    
print(answer)