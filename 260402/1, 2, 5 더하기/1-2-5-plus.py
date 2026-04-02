n = int(input())

# Please write your code here.
num = [1, 2, 5]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n + 1):
    for j in num:
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i - j]) % 10007

print(dp[n])