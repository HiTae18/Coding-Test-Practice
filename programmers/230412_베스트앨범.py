def solution(genres, plays):
    answer = []
    music = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        music[genre] = music.get(genre, []) + [[play, i]]

    for genre in music.keys():
        music[genre].sort(key=lambda x: -x[0])
        music[genre] += [sum(list(map(lambda x: x[0], music[genre])))]

    for _, values in sorted(music.items(), key=lambda x: -x[1][-1]):
        answer.append(values[0][1]) if len(
            values[:-1]) == 1 else answer.extend([values[0][1], values[1][1]])

    return answer
