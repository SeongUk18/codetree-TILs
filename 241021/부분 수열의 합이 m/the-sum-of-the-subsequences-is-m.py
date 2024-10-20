# 입력 받기
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

dp = [float('inf') for _ in range(m + 1)]

dp[0] = 0

for i in range(1, n):
    for j in range(m - 1, -1, -1):
        if num_list[i] <= j:
            dp[j] = min(dp[j], dp[j - num_list[i]] + 1)

if dp[m - 1] == float('inf'):
    print(-1)
else:
    print(dp[m - 1])