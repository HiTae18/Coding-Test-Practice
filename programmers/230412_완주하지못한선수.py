def solution(participant, completion):

    people = {}
    for p in participant:
        people[p] = people.get(p, 0) + 1

    for p in completion:
        people[p] -= 1
        if people[p] == 0:
            people.pop(p)

    return next(iter(people.keys()))
