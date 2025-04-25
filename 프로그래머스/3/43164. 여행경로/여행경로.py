def solution(tickets):
    from collections import defaultdict

    graph = defaultdict(list)

    # 티켓 정보를 그래프로 만들되, 도착지를 알파벳 역순으로 정렬해서 스택처럼 pop()
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        route.append(airport)

    dfs("ICN")
    return route[::-1]  # 역순으로 방문 결과 리턴
