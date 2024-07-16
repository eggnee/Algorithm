N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

r = len(A)
flag = False
tmp = [0] * r
saveCount = 0

def merge_sort(A, p, r): # A 배열을 오름차순 정렬한다.
    if flag == True:
        return
    if p < r:
        q = (p + r) // 2;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합 정렬


def merge(A, p, q, r):
    global tmp
    global saveCount
    global K
    global flag
    i = p
    j = q + 1
    t = 0
    
    while (i <= q and j <= r):
        if (A[i] <= A[j]):
            tmp[t] = A[i] # tmp[t] = A[i]; t++; i++;
            i = i + 1
        else:
            tmp[t] = A[j] # tmp[t] = A[j]; t++; j++;
            j = j + 1
        t = t + 1
        
    
    while (i <= q): # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        t = t + 1
        i = i + 1
    while (j <= r):  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        t = t + 1
        j = j + 1
    
    i = p
    t = 0
    
    while (i <= r):  # 결과를 A에 저장
        A[i] = tmp[t]
        saveCount = saveCount + 1
        if saveCount == K:
            print(A[i])
            flag = True
            return
        i = i + 1
        t = t + 1
        
merge_sort(A, 0, r-1)
if flag == False:
    print(-1)

