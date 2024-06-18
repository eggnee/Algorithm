K = int(input()) #반복 횟수 입력
numList = []
for i in range(0, K):
    num = input()
    if num == "0":
        numList.pop(-1)
    else:
        numList.append(num)

hap = 0
for i in numList:
    hap += int(i)

print(hap)
