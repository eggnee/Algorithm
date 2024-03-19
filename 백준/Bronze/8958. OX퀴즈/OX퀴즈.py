t = int(input())
for _ in range(t):
    result = 0
    oNum = 0
    test = list(input())
    for i in test:
        if i == 'O':
            oNum += 1
        else:
            oNum = 0
        result += oNum
    print(result)
            
    