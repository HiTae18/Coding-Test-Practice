from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        cur_price = prices.popleft()
        second = 0
        
        # 가격이 하락하지 않을 때까지 반복 
        for price in prices:
            second += 1
            if cur_price <= price:
                continue
            else:
                break
        answer.append(second)
    return answer