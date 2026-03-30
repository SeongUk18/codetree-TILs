n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
dp = [-1] * n

dp[0] = 0

for i in range(n):
    for j in range(i):
        if dp[j] == -1:
            continue 

        if j + m[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))