n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
dp = [1] * n

for i in range(n):
    for j in range(i, n):
        if m[i] < m[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))