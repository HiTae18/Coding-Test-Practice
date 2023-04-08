from collections import deque


def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])

    dist = deque()
    dist.append((0, 0))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while maps[-1][-1] == 1 and dist:
        cur_x, cur_y = dist.popleft()

        for x, y in zip(dx, dy):
            next_x, next_y = cur_x + x, cur_y + y
            if 0 <= next_x < n and 0 <= next_y < m:
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] += maps[cur_x][cur_y]
                    dist.append((next_x, next_y))

    answer = -1 if maps[-1][-1] == 1 else maps[-1][-1]

    return answer
