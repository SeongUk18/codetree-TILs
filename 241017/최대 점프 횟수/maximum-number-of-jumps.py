n = int(input())

n_list = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if j + n_list[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))