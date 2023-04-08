from collections import deque


def solution(begin, target, words):
    visited = [False] * len(words)

    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        word, loc = queue.popleft()
        if word == target:
            return loc

        for i in range(len(words)):
            if not visited[i] and is_possible(word, words[i]):
                queue.append([words[i], loc+1])
                visited[i] = True

    return 0


def is_possible(word_a, word_b):
    flag = 0
    for i in range(len(word_a)):
        if word_a[i] != word_b[i]:
            flag += 1
        if flag > 1:
            return False
    return True
