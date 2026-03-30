n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
lines = list(zip(x1, x2))
lines.sort()

dp = [1] * n

for i in range(n):
    for j in range(i + 1, n):
        if lines[j][0] > lines[i][1]:
            dp[i] = max(dp[i] + 1, dp[j])

print(max(dp))