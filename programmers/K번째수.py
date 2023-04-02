def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command
        # i번째부터 j까지 slice하고 sorted된 배열에서 k번째 index값을 answer에 추가
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))