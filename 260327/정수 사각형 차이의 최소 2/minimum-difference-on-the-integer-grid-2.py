n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = float('inf')

for low in range(1, 101):
    if grid[0][0] < low:
        continue

    dp = [[float('inf') for _ in range(n)] for _ in range(n)]

    dp[0][0] = grid[0][0]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            
            if grid[i][j] < low:
                continue

            prev = 101

            if i > 0:
                prev = min(dp[i - 1][j], prev)
            if j > 0:
                prev= min(dp[i][j - 1], prev)

            if prev != 101:
                dp[i][j] = max(prev, grid[i][j])

    if dp[n - 1][n - 1] != float('inf'):
        answer = min(answer, dp[n - 1][n - 1] - low)

print(answer)