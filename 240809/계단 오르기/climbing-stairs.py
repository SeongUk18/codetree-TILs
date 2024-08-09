n = int(input())

def sol(n):
    if n < 2:
        return 0

    # DP 테이블 초기화
    dp = [0] * (n + 1)


    if n >= 2:
        dp[2] = 1 

    if n >= 3:
        dp[3] = 1

    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    return dp[n]

print(sol(n))