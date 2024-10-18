# 입력 받기
n, m = map(int, input().split())

coin_list = list(map(int, input().split()))

# DP 테이블 초기화
dp = [float('inf') for _ in range(m + 1)]
dp[0] = 0

# DP 테이블 생성
for i in range(1, m + 1):
    for j in range(n):
        if coin_list[j] <= i:
            dp[i] = min(dp[i], dp[i - coin_list[j]] + 1)

print(dp[m])