import sys

input = sys.stdin.readline

N = int(input().strip())

words = [input().strip() for _ in range(N)]


def solution(N, words):
    alphabets = {}
    for word in words:
        for i, alphabet in enumerate(word[::-1]):
            alphabets[alphabet] = alphabets.get(alphabet, 0) + 10**i

    sorted_alphabet = sorted(alphabets.items(), key=lambda x: x[1], reverse=True)

    num = 9

    for alphabet, _ in sorted_alphabet:
        for i in range(len(words)):
            words[i] = words[i].replace(alphabet, str(num))
        num -= 1

    result = 0
    for word in words:
        result += int(word)

    return result


print(solution(N, words))
