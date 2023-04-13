def solution(m, n, puddles):
    maps = {}

    for x, y in puddles:
        maps[(x, y)] = 0

    maps[(1, 1)] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            maps[(i, j)] = maps.get((i, j), maps.get((i-1, j), 0) + maps.get((i, j-1), 0))

    return maps[(m, n)] % 1000000007
