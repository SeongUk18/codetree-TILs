N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
dp = [-1] * (M + 1)
dp[0] = 0

for i in range(M + 1):
    for c in coin:
        if dp[i - c] == -1:
            continue

        if i - c >= 0:
            dp[i] = max(dp[i], dp[i - c] + 1)

print(dp[M])