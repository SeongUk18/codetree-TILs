n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.
profit = [0] + profit
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp[j] = max(dp[j], dp[j - i] + profit[i])
        

print(dp[n])