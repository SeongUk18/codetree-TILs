n = int(input())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

# dp 배열 생성
dp = [[0 for _ in range(n)] for _ in range(n)]
# print(dp)
for i in range(n):
    for j in range(n - 1, -1, -1):
        # print(i, j, map_list[i][j])
        if i == 0 and j == n - 1:
            dp[i][j] = map_list[i][j]
            # print(dp[i][j])
        elif i == 0 and j < n:
            dp[i][j] = map_list[i][j] + dp[i][j + 1]
            # print(dp[i][j])
        elif j == n -1:
            dp[i][j] = map_list[i][j] + dp[i - 1][j]
        else:
            dp[i][j] = map_list[i][j] + min(dp[i][j + 1], dp[i - 1][j])

# 최종 값 출력
print(dp[n - 1][0])