def solution(nums):
    ponkemon = {}

    for num in nums:
        ponkemon[num] = ponkemon.get(num, 0) + 1

    choice = len(nums) // 2
    speices = len(ponkemon.keys())

    return speices if choice >= speices else choice
