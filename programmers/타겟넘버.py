def solution(numbers, target):
    
    return dfs(target, 0, numbers)


def dfs(target, current, numbers):
    if not numbers:
        return 1 if target == current else 0
    return dfs(target, current + numbers[0], numbers[1:]) + dfs(target, current - numbers[0], numbers[1:])