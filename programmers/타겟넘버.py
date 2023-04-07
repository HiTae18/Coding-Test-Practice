def solution(numbers, target):
    global answer
    answer = 0
    dfs(target, 0, numbers)
    return answer


def dfs(target, current, numbers):
    global answer
    if not numbers:
        if current == target:
            answer += 1
            return
        return

    dfs(target, current + numbers[0], numbers[1:])
    dfs(target, current - numbers[0], numbers[1:])


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))
