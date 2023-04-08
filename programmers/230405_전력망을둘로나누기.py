def solution(n, wires):
    answer = 99
    connect = {}
    for i in range(n):
        connect[i+1] = []
    for w, v in wires:
        connect[w].append(v)
        connect[v].append(w)

    for w, v in wires:
        connect[w].remove(v)
        connect[v].remove(w)
        diff = abs(n_connect(w, connect, [w]) - n_connect(v, connect, [v]))
        if diff < answer:
            answer = diff
        connect[w].append(v)
        connect[v].append(w)
    return answer


def n_connect(n, connect, visted):
    for ele in connect[n]:
        if ele not in visted:
            visted.append(ele)
            n_connect(ele, connect, visted)
    return len(visted)
