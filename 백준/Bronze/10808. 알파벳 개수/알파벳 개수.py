s = input()
alpha = [0 for _ in range(26)]
for i in list(str(s)):
    alpha[ord(i)-97] += 1

print(' '.join(map(str, alpha)))
