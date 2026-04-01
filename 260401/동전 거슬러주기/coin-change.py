N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
dp = [float('inf')] * (M + 1)
dp[0] = 0

for c in coin:
    for i in range(c, M + 1):
        if dp[i - c] != float('inf'):
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[M] == float('inf'):
    print(-1)
else:
    print(dp[M])