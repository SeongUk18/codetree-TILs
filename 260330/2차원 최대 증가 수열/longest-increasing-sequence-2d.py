n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[-1 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(m):

        for a in range(i + 1, n):
            for b in range(j + 1, m):
                if dp[i][j] == -1:
                    continue

                if grid[i][j] < grid[a][b]:
                    dp[a][b] = max(dp[a][b], dp[i][j] + 1)

answer = 0
for arr in dp:
    answer = max(max(arr), answer)

print(answer)