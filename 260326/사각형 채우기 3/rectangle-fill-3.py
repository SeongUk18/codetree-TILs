n = int(input())

# Please write your code here.
dp = [0] * (n + 1)
dp[0] = 2

for i in range(1, n + 1):
    dp[i] = dp[i - 1] * 3 + 1

print(dp[n - 1] % 1000000007)