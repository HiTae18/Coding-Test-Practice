import sys

input = sys.stdin.readline


def solution(k, signs):
    global available
    available = []

    for i in range(0, 10):
        dfs(k, [i], signs)

    return (available[-1], available[0])


def dfs(k, nums, signs):
    global available
    if len(nums) == k+1:
        available.append("".join(list(map(str, nums))))
        return
    for i in range(0, 10):
        if i not in nums:
            if signs[0] == ">":
                dfs(k, nums + [i], signs[1:]) if nums[-1] > i else None
            else:
                dfs(k, nums + [i], signs[1:]) if nums[-1] < i else None


k = int(input().strip())
signs = input().split
answer = solution(k, signs)
print(answer[0])
print(answer[1])
