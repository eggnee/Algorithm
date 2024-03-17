t = int(input())

stairs = [0]
d = [0 for _ in range(t+1)]

for _ in range(t):
    stairs.append(int(input()))

for i in range(1, t+1):
    if i <= 2:
        d[i] = d[i-1] + stairs[i]
    else:
        d[i] = max(d[i-3] + stairs[i-1] + stairs[i], d[i-2] + stairs[i])

print(d[-1])