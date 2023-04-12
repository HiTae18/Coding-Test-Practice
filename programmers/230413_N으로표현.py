def solution(N, number):
    answer = 0
    num_dict = {}

    while answer < 8:
        answer += 1
        only_N = int(str(N)*answer)
        if only_N == number:
            return answer
        num_dict[answer] = {only_N}

        for i in range(1, answer//2+1):
            for left in num_dict[i]:
                for right in num_dict[answer-i]:
                    temp = {left + right, left - right, right - left, left * right}
                    temp.update({0} if not left or not right else {left // right, right // left})
                    if number in temp:
                        return answer
                    num_dict[answer].update(temp)
    return -1
