N = int(input())

dp = [0] * (N + 1)

dp[0] = 1

if N < 2:
    print(0)
    exit()
for i in range(2, N + 1):
    if i >= 2:
        dp[i] += dp[i - 2]
    if i >= 3:
        dp[i] += dp[i - 3]

print(dp[N] % 10007)