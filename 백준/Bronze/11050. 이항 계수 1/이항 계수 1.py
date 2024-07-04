N, K = list(map(int, input().split()))

def fac(num):
    answer = 1
    for i in range(2, num+1):
        answer = answer * i
    return answer

print(fac(N) // (fac(N-K) * fac(K)))