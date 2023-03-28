from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 현재 대기 중인 트럭과 다리를 지나고 있는 트럭 리스트를 큐로 만듦.
    waiting_truck = deque(truck_weights)
    current_truck = deque()
    
    # 현재 다리에 있는 트럭의 무게를 저장하는 변수
    current_weight = 0
    
    # 모든 트럭이 다리를 지났을 때만 반복문 종료
    while current_truck or waiting_truck:
        answer += 1
        
        # 다리를 지나고 있는 트럭의 위치가 bridge_length의 끝일 경우 트럭을 내보냄.
        if current_truck and current_truck[0][1] == bridge_length:
            [truck, _] = current_truck.popleft()
            current_weight -= truck
        
        # 현재 다리를 지나고 있는 트럭들의 위치를 1씩 증가
        for i in range(len(current_truck)):
            current_truck[i][1] += 1
        
        # 대기 중인 트럭이 있으며, 다음 트럭이 다리 위를 올라올 수 있는 경우에만 popleft()
        if waiting_truck and weight >= current_weight + waiting_truck[0]:
            truck = waiting_truck.popleft()
            current_truck.append([truck,1])
            current_weight += truck
             
    return answer