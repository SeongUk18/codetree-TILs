N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [0] * (M + 1)


for j in range(N):
    for i in range(M, w[j] - 1, -1):
        dp[i] = max(dp[i], dp[i - w[j]] + v[j])

print(dp[M])