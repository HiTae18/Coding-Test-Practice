from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = [[0] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]

    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2, (x2)*2+1):
            for j in range(y1*2, (y2)*2+1):
                maps[i][j] = 1

    queue = deque([[characterX*2, characterY*2, 0]])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:

        cur_x, cur_y, move = queue.popleft()
        if cur_x == itemX * 2 and cur_y == itemY * 2:
            answer = move // 2
            break
        for x, y in zip(dx, dy):
            next_x, next_y = cur_x + x, cur_y + y
            if maps[next_x][next_y] and not visited[next_x][next_y] and is_line(next_x, next_y, maps):
                visited[next_x][next_y] = True
                queue.append([next_x, next_y, move+1])

    return answer


def is_line(x, y, maps):
    result = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            result += maps[i][j]

    if result >= 9:
        return False
    return True
