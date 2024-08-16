n = int(input())

dp = [[_ for _ in range(n)] for _ in range(n)]

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

# DP 생성
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = map_list[i][j]
        elif j == 0:
            dp[i][j] = map_list[i][j] + dp[i - 1][j]
        else:
            dp[i][j] = max(map_list[i][j] + dp[i - 1][j], map_list[i][j] + dp[i][j - 1])

# print(dp)
# 마지막 값 출력
print(dp[n - 1][n - 1])