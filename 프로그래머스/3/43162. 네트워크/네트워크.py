def solution(n, computers):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)

    # 루트 정리
    for i in range(n):
        parent[i] = find(i)

    return len(set(parent))
