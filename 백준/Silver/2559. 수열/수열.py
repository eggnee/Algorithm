N, K = map(int, input().split())
number = list(map(int, input().split()))

answer = sum(number[0:K])
hap = answer
for i in range(K, N):
    hap -= number[i-K]
    hap += number[i]
    answer = max(answer, hap)

print(answer)