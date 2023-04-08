def solution(brown, yellow):
    options = []
    total = brown + yellow

    for i in range(yellow, int(yellow ** 0.5) - 1, -1):
        w = i
        h = yellow // i

        if w * h == yellow:
            options.append((w, h))

    for w, h in options:
        if (w + 2) * (h + 2) == total:
            return [w + 2, h + 2]
