t = int(input())
for _ in range(t):
    n = int(input())
    n = list(format(n, 'b')) # 이진수로 변환
    n.reverse()
    for i in range(len(n)):
        if n[i] == '1':
            print(i, end=" ")