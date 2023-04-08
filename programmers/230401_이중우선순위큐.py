from collections import deque
from heapq import heappush, heappop

def solution(operations):
    answer = []
    
    operations = deque(operations)
    
    min_heap = []
    max_heap = []
    numbers = {}
    
    while operations:
        op,data = operations.popleft().split()
        
        # Operation이 Insert일 때, 최소 힙과 최대 힙에 push, numbers dictionary에 해당 key가 존재한다면 +1, 없다면 key, value 생성
        if op == "I":
            data = int(data)
            heappush(min_heap, data)
            heappush(max_heap, -data)
            
            if data not in numbers:
                numbers[data] = 1
            else:
                numbers[data] += 1
        
        # Operation이 Delete일 때, 최솟값, 최댓값 제거 경우를 나누고 각 힙에서 pop, 해당 number가 존재한다면 numbers에서 -1, 값이 0이라면 key 삭제
        elif numbers:
            if data == "-1":
                num = heappop(min_heap)
                if numbers[num]:
                    numbers[num] -= 1
                    if numbers[num] == 0:
                        del numbers[num]
            else:
                num = -heappop(max_heap)
                if numbers[num]:
                    numbers[num] -= 1
                    if numbers[num] == 0:
                        del numbers[num]
        
        # Operation이 Delete이지만 numbers가 존재하지 않는 경우, 힙을 비워줌
        else:
            min_heap, max_heap = [], []
            
    if not numbers:
        answer = [0, 0]
    else:
        answer = [max(numbers), min(numbers)]
    
    return answer

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))