# 입력
n = int(input())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

# DP 생성
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = map_list[0][0]
for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], map_list[i][0])
        dp[0][i] = min(dp[0][i - 1], map_list[0][i])

# print(dp)

for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i - 1][j], map_list[i][j]), min(dp[i][j - 1], map_list[i][j]))

# 출력
# print(dp)
print(dp[n - 1][n - 1])