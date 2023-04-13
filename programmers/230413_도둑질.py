def solution(money):
    answer = 0
    dp_f = [money[0], money[0]]
    dp_l = [0, money[1]]

    for i, mone in enumerate(money):
        if i >= 2:
            dp_f = [dp_f[1], max(dp_f[1], mone + dp_f[0])]
            dp_l = [dp_l[1], max(dp_l[1], mone + dp_l[0])]
    return max(dp_f[0], dp_l[1])
