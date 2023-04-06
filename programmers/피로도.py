def solution(k, dungeons):
    global answer
    answer = -1
    visit = 0
    brute_force(k, visit, dungeons)
    return answer


def brute_force(k, visit, dungeons):
    global answer

    if k < 0:
        return
    if len(dungeons) == 0:
        if visit > answer:
            answer = visit
            return
    print(dungeons)
    for i in range(len(dungeons)):
        dungeon = dungeons[i]
        dungeons.pop(i)
        if k >= dungeon[0]:
            brute_force(k - dungeon[1], visit+1, dungeons)
        else:
            brute_force(k, visit, dungeons)
        dungeons.insert(i, dungeon)
