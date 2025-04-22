import sys
sys.setrecursionlimit(20000)

N = int(input())
people_number = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

select = [people_number[i] for i in range(N + 1)]        # 해당 마을을 우수 마을로 선택한 경우
unselect = [0] * (N + 1)      # 해당 마을을 우수 마을로 선택하지 않은 경우

def dfs(current, parent):
    for child in graph[current]:
        if child != parent:
            dfs(child, current)
            unselect[current] += max(select[child], unselect[child])
            select[current] += unselect[child]

dfs(1, -1)

print(max(select[1], unselect[1]))
