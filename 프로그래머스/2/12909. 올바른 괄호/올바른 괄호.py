def solution(s):
    stack = []
    for temp in s:
        if temp == "(":
            stack.append(temp)
        else:
            if not stack or (stack and stack[-1] != "("):
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True