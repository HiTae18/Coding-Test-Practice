import sys

input = sys.stdin.readline


def solution(k, signs):
    global available, found

    numbers = [i for i in range(9, -1, -1)]

    found = False
    for i in numbers:
        dfs(k, [i], numbers, signs)

    found = False

    numbers.reverse()
    for i in numbers:
        dfs(k, [i], numbers, signs)

    return


def dfs(k, nums, numbers, signs):
    global available, found
    if found:
        return

    if len(nums) == k+1:
        # available.append("".join(list(map(str, nums))))
        print("".join(list(map(str, nums))))
        found = True
        return
    for i in numbers:
        if i not in nums:
            if signs[0] == ">":
                dfs(k, nums + [i], numbers, signs[1:]) if nums[-1] > i else None
            else:
                dfs(k, nums + [i], numbers, signs[1:]) if nums[-1] < i else None


k = int(input().strip())
signs = input().split()

answer = solution(k, signs)
