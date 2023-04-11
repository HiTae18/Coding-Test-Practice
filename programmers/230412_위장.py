def solution(clothes):
    answer = 1
    clothes_dict = {}

    for c, kind in clothes:
        clothes_dict[kind] = clothes_dict.get(kind, []) + [c]

    for cnt in clothes_dict.values():
        answer *= len(cnt) + 1

    return answer - 1
