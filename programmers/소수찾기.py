from itertools import permutations


def solution(numbers):
    answer = 0

    for n in range(len(numbers)):
        for num in set(["".join(ele) for ele in list(permutations(numbers, n+1))]):
            if not num.startswith("0"):
                answer += 1 if isPrime(int(num)) else 0

    return answer


def isPrime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
