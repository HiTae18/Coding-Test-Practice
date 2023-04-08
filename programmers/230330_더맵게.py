import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    # 섞는 것은 음식의 개수가 2개 이상이며, 가장 작은 스코빌 지수가 K보다 작을 때만 반복한다.
    while len(scoville) >= 2 and scoville[0] < K :
        heapq.heappush(scoville, heapq.heappop(scoville) + 2 * heapq.heappop(scoville))
        answer += 1
    
    # while문 을 나왔을 때 스코빌 지수가 가장 큰 값이 K보다 작다면 -1을 return
    if scoville[-1] < K:
        return -1
    return answer