def getPosition(d, p):
    if d == 1:
        return((d, [0, p]))
    elif d == 3:
        return((d, [p, 0]))
    elif d == 2:
        return((d, [row, p]))
    else:
        return((d, [p, column]))

column, row = map(int, input().split())
shopNumber = int(input())
shops = []
for _ in range(shopNumber):
    d, p = map(int, input().split())
    pos = getPosition(d, p)
    shops.append(pos)

d, p = map(int, input().split())
dongun = getPosition(d, p)
answer = 0

for temp in shops:
    d = temp[0]
    
    if d + dongun[0] == 3 or d + dongun[0] == 7: # 맞은편의 경우
        if d in [1, 2]:
            case1, case2 = 0, 0
            case1 = temp[1][0] + temp[1][1] + dongun[1][1] + dongun[1][0]
            case2 = temp[1][0] + (column-temp[1][1]) + dongun[1][0] + (column-dongun[1][1])
            answer += min(case1, case2)
        else:
            case1, case2 = 0, 0
            case1 = temp[1][0] + temp[1][1] + dongun[1][1] + dongun[1][0]
            case2 = temp[1][1] + (row-temp[1][0]) + dongun[1][1] + (row-dongun[1][0])
            answer += min(case1, case2)
        
    else:
        for i in range(2):
            answer += abs(temp[1][i] - dongun[1][i])

print(answer)

