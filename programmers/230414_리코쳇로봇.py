from collections import deque


def solution(board):
    answer = 0

    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_x, start_y = i, j
            elif board[i][j] == 'G':
                goal_x, goal_y = i, j

    queue = deque()
    queue.append([start_x, start_y, 0])
    visited[start_x][start_y] = True
    while queue:
        cur_x, cur_y, cnt = queue.popleft()
        for x, y in zip(dx, dy):
            next_x, next_y = cur_x + x, cur_y + y
            while True:
                # 그 방향으로 계속 진행하면서 장애물을 마주치거나 더 이상 진행할 수 없는 방향인 경우
                if not (0 <= next_x < n and 0 <= next_y < m) or board[next_x][next_y] == 'D':
                    break
                next_x += x
                next_y += y
            # 멈췄는데 골인지점이면 종료
            if board[next_x-x][next_y-y] == 'G':
                return cnt + 1
            # 멈춘지점의 visted가 방문되지 않았을 때만 True
            if not visited[next_x-x][next_y-y]:
                visited[next_x-x][next_y-y] = True
                queue.append([next_x-x, next_y-y, cnt + 1])
    return -1
