def solution(n, lost, reserve):
    answer = 0
    own = 0

    lost.sort()
    reserve.sort()

    # 여벌 체육복이 있으면서 도난 당한 경우 lost, reserve에서 제외
    new_reserve = list(set(reserve) - set(lost))
    new_lost = list(set(lost) - set(reserve))

    for st in new_lost:
        if st-1 in new_reserve:
            own += 1
            new_reserve.remove(st-1)
        elif st+1 in new_reserve:
            own += 1
            new_reserve.remove(st+1)

    answer = n - len(new_lost) + own
    return answer
