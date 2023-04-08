def solution(citations):
    citations.sort(reverse = True)
    answer = len(citations)
    
    for h,citation in enumerate(citations):
        # 인용횟수가 논문의 수 보다 작아지는 경우가 H-index
        if citation < h + 1:
            return h
    # 인용횟수가 논문의 수 보다 작아지는 경우가 없으면 H-index는 전체 논문의 수와 같다.
    return answer



citations = [3,3, 0, 6, 1, 5]
print(solution(citations))

