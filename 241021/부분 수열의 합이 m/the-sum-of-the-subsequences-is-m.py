# 입력 받기
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

dp = [float('inf') for _ in range(m + 1)]

dp[0] = 0

for i in range(n):
    for j in range(m, num_list[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - num_list[i]] + 1)

if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])