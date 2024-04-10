freq = [0] * 10

A = int(input())
B = int(input())
C = int(input())

for i in str(A*B*C):
    freq[int(i)] += 1

for i in freq:
    print(i)
