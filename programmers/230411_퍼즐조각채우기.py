from collections import deque

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    board_block = find_block(game_board, 0, n)
    table_block = find_block(table, 1, n)

    for size, block in board_block.items():
        if size in table_block:
            for board in block:
                cnt = len(table_block[size])
                while table_block[size] and cnt > 0:
                    table = table_block[size].pop(0)
                    if is_fill(board, table):
                        answer += size
                        break
                    table_block[size].append(table)
                    cnt -= 1

    return answer

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def is_fill(board, table):
    rotates = [table, rotate_matrix(table), rotate_matrix(
        rotate_matrix(table)), rotate_matrix(rotate_matrix(rotate_matrix(table)))]
    return any(board == matrix for matrix in rotates)

def find_block(maps, sign, n):
    queue = deque()
    block_dict = {}

    for i in range(n):
        for j in range(n):
            if maps[i][j] == sign:
                maps[i][j] = (sign + 1) % 2
                queue.append([i, j])
                temp = []
                while queue:
                    cur_x,  cur_y = queue.popleft()
                    temp.append([cur_x, cur_y])
                    for x, y in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                        next_x, next_y = cur_x + x, cur_y + y
                        if (0 <= next_x < n and 0 <= next_y < n) and maps[next_x][next_y] == sign:
                            maps[next_x][next_y] = (sign + 1) % 2
                            queue.append([next_x, next_y])

                x_min, x_max = min(temp, key=lambda x: x[0])[0], max(temp, key=lambda x: x[0])[0]
                y_min, y_max = min(temp, key=lambda x: x[1])[1], max(temp, key=lambda x: x[1])[1]

                matrix = [[0] * (y_max - y_min + 1) for _ in range(x_max - x_min + 1)]

                for x, y in temp:
                    matrix[x - x_min][y - y_min] = 1

                block_dict[len(temp)] = block_dict.get(len(temp), []) + [matrix]
    return dict(sorted(block_dict.items()))