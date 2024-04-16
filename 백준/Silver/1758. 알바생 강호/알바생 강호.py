import sys
input = sys.stdin.readline

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num.sort(reverse=True)

rank = 1
answer = 0
for i in num:
    if i - (rank-1) >= 0:
        answer += i - (rank-1)
    rank += 1

print(answer)
