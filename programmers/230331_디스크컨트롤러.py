from collections import deque
from heapq import heapify, heappop, heappush


def solution(jobs):
    answer = 0
    
    current_time = 0
    n = len(jobs)
    available = []
    
    # 요청 시간 기준으로 정렬
    jobs.sort()
    jobs = deque(jobs)
    
    while jobs or available:
        # 요청된 작업이 없으면 가장 가까운 요청 시간으로 current_time을 설정
        if not available and jobs[0][0] > current_time:
            current_time = jobs[0][0]

        # 현재 시간에서 수행 가능한 job을 힙에 push
        while jobs and jobs[0][0] <= current_time:
            start, time = jobs.popleft()
            heappush(available, [time, start])

        # 가능한 작업 중 time이 가장 짧은 순서부터 pop
        if available:
            time, start = heappop(available)
            current_time += time
            answer += current_time - start

    return answer // n