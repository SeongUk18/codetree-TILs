n, m = map(int, input().split())

coin_list = list(map(int, input().split()))

dp = [float('-inf') for _ in range(m + 1)]
dp[0] = 0

for i in range(len(coin_list)):
    for j in range(1, m + 1):
        if j >= coin_list[i]:
            dp[j] = max(dp[j], dp[j - coin_list[i]] + 1)

print(dp[m])