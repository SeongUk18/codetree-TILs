n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
up_dp = [0] * n
down_dp = [0] * n

for i in range(n):
    up_dp[i] = 1
    for j in range(i):
        if sequence[j] < sequence[i]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)

for i in range(n - 1, -1, -1):
    down_dp[i] = 1
    for j in range(i + 1, n):
        if sequence[j] < sequence[i]:
            down_dp[i] = max(down_dp[i], down_dp[j] + 1)

dp = [0] * n
for i in range(n):
    dp[i] = up_dp[i] + down_dp[i] - 1

print(max(dp))