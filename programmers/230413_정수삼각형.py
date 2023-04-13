def solution(triangle):
    dp = []
    for t in triangle:
        dp = [0] + dp + [0]
        dp = [value + max(dp[i], dp[i+1]) for i, value in enumerate(t)]
    return max(dp)
