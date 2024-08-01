maxNum = -1
peopleNum = 0
for _ in range(10):
    minus, plus = map(int, input().split())
    peopleNum = peopleNum + (-minus) + plus
    if peopleNum > maxNum :
        maxNum = peopleNum

print(maxNum)