n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dp = [0] * n

for i in range(n):
    dp[i] = arr[i]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i - 1] + arr[i])

print(dp[n - 1])