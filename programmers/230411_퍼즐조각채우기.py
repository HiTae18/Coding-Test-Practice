from collections import deque


def solution(game_board, table):
    answer = 0
    n = len(game_board)

    board_block = find_block(game_board, 0, [[False] * n for _ in range(n)], n)

    table_block = find_block(table, 1, [[False] * n for _ in range(n)], n)

    for i, block in board_block.items():
        if i in table_block:
            for board in board_block[i]:
                cnt = len(table_block[i])
                while table_block[i]:
                    if cnt == 0:
                        break
                    table = table_block[i].pop(0)
                    if is_fill(board, table):
                        answer += i
                        break
                    else:
                        table_block[i].append(table)
                    cnt -= 1

    return answer


def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def is_fill(board, table):
    rotates = [table, rotate_matrix(table), rotate_matrix(
        rotate_matrix(table)), rotate_matrix(rotate_matrix(rotate_matrix(table)))]
    return any(board == matrix for matrix in rotates)


def find_block(maps, sign, visited, n):
    queue = deque()
    block_dict = {}
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == sign and visited[i][j] == False:
                visited[i][j] = True
                queue.append([i, j])
                temp = []
                while queue:
                    cur_x,  cur_y = queue.popleft()
                    temp.append([cur_x, cur_y])

                    for x, y in zip(dx, dy):
                        next_x, next_y = cur_x + x, cur_y + y
                        if (0 <= next_x < n and 0 <= next_y < n) and not visited[next_x][next_y] and maps[next_x][next_y] == sign:
                            visited[next_x][next_y] = True
                            queue.append([next_x, next_y])

                x_min = min(temp, key=lambda x: x[0])[0]
                x_max = max(temp, key=lambda x: x[0])[0]
                y_min = min(temp, key=lambda x: x[1])[1]
                y_max = max(temp, key=lambda x: x[1])[1]

                matrix = [[0] * (y_max - y_min + 1) for _ in range(x_max - x_min + 1)]

                for x, y in temp:
                    matrix[x - x_min][y - y_min] = 1

                block_dict[len(temp)] = block_dict.get(len(temp), []) + [matrix]
    return dict(sorted(block_dict.items()))
