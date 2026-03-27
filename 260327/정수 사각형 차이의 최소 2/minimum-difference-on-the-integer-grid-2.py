n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[(101, 0) for _ in range(n)] for _ in range(n)]

dp[0][0] = (grid[0][0], grid[0][0])

for i in range(1, n):
    dp[0][i] = (min(grid[0][i], dp[0][i - 1][0]), max(grid[0][i], dp[0][i - 1][1]))
    dp[i][0] = (min(grid[i][0], dp[i - 1][0][0]), max(grid[i][0], dp[i - 1][0][1]))

# print(dp)

for i in range(1, n):
    for j in range(1, n):
        if abs(max(dp[i - 1][j][1], grid[i][j]) - min(dp[i - 1][j][0], grid[i][j])) >= abs(max(dp[i][j - 1][1], grid[i][j]) - min(dp[i][j - 1][0], grid[i][j])):
            dp[i][j] = (min(dp[i][j - 1][0], grid[i][j]), max(dp[i][j - 1][1], grid[i][j]))
        else:
            dp[i][j] = (min(dp[i - 1][j][0], grid[i][j]), max(dp[i - 1][j][1], grid[i][j]))
print(dp[n - 1][n - 1][1] - dp[n - 1][n - 1][0])