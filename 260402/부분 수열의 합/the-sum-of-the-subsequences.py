n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
dp = [0] * (m + 1)
dp[0] = 1

for num in A:
    for i in range(m, num - 1, -1):
        if dp[i - num] != 0:
            dp[i] = max(dp[i], dp[i - num] + 1)

if dp[m] == 0:
    print("No")
else:
    print("Yes")