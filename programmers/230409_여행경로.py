def solution(tickets):
    global min_route
    min_route = "ZZZZ"

    visited = [False] * len(tickets)
    dfs("ICN", "ICN", tickets, visited)
    answer = [min_route[i:i+3] for i in range(0, len(min_route), 3)]
    return answer


def dfs(route, current, tickets, visited):
    global min_route
    if len(route) == (len(tickets) + 1) * 3:
        min_route = route if route < min_route else min_route
        return

    for i in range(len(tickets)):
        if not visited[i] and tickets[i][0] == current:
            visited[i] = True
            dfs(route + tickets[i][1], tickets[i][1], tickets, visited)
            visited[i] = False
