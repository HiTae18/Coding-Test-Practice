def solution(word):
    global s
    answer = 0
    words = "AEIOU"
    s = []
    create_word("", words)
    answer = s.index(word)
    return answer


def create_word(current_word, words):
    global s
    if len(current_word) > 5:
        return
    else:
        s.append(current_word)
    for word in words:
        create_word(current_word+word, words)
