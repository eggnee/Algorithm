height = []
flag = True

for _ in range(9):
    height.append(int(input()))

gap = sum(height) - 100
for i in range(8):
    for j in range(i+1, 9):
        a = height[i]
        b = height[j]
        if a + b == gap:
            height.remove(a)
            height.remove(b)
            flag = False
            break
    if flag == False:
        break

height.sort()

for i in height:
    print(i)
