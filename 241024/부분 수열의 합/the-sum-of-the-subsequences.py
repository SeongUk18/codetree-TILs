n, m = map(int, input().split())

num_list = list(map(int, input().split()))

dp = [0 for _ in range(m + 1)]

dp[0] = 1

for i in range(n):
    for j in range(m, num_list[i] - 1, -1):
        if dp[j - num_list[i]]:
            dp[j] = 1

if dp[m]:
    print("Yes")
else:
    print("No")