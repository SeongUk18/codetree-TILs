n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
dp = [float('inf')] * (m + 1)
dp[0] = 0

for num in A:
    for i in range(m, num - 1, -1):
        if dp[i - num] == float('inf'):
            continue

        dp[i] = min(dp[i - num] + 1, dp[i])

if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])