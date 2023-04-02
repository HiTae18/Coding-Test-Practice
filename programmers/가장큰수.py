def solution(numbers):
    
    numbers = [str(num) for num in numbers]
    
    # ex) 5, 557 => 555, 5575577 => 557이 5보다 앞 순서로 옴
    numbers.sort(key = lambda x: x + x + x[-1], reverse=True)
    
    answer = ''.join(numbers)
    
    if answer.startswith('0'):
        answer = '0'
    
    return answer
