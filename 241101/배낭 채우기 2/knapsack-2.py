n, m = map(int, input().split())

weights = []
values = []

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [0 for _ in range(m + 1)]

for i in range(n):
    for j in range(weights[i], m + 1):
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

print(dp[m])