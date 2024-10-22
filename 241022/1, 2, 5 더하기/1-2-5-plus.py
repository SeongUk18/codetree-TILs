n = int(input())

num_list = [1, 2, 5]

dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]  # 1을 사용한 경우
        if i >= 2:
            dp[i] += dp[i - 2]  # 2를 사용한 경우
        if i >= 5:
            dp[i] += dp[i - 5]  # 5를 사용한 경우



print(dp[n] % 10007)