def solution(sizes):
    answer = 0
    w_list, h_list = [], []

    for w,h in sizes:
        w_list.append(max(w,h))
        h_list.append(min(w,h))
    
    answer = max(w_list) * max(h_list)
    
    return answer