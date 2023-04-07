from collections import deque


def solution(n, computers):
    global visited
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers)

    return answer


def dfs(i, computers):
    global visited
    for idx, computer in enumerate(computers[i]):
        if not visited[idx] and computer:
            visited[idx] = True
            dfs(idx, computers)


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))
