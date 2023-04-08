from collections import deque

def solution(priorities, location):
    answer = 0
    # 큐에 (우선순위, 각 location을) 저장
    queue = deque([(prior, idx) for idx, prior in enumerate(priorities)])
        
    while queue:
        j = queue.popleft()
        
        # J가 나머지 인쇄 대기목록보다 중요도가 가장 높은지 검사
        if queue and max(queue)[0] > j[0]:
            # 대기목록의 가장 마지막으로 보냄
            queue.append(j)
        else:
            # 랭크를 증가시키고, location이 일치한다면 반복문 종료
            answer += 1
            if j[1] == location:
                break
                
    return answer