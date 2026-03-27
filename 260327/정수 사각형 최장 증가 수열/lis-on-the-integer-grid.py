n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cells = []
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

cells.sort()

dp = [[1 for _ in range(n)] for _ in range(n)]

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

for val, i, j in cells:
    for k in range(4):
        x = j + x_list[k]
        y = i + y_list[k]

        if 0 <= x < n and 0 <= y < n:
            if grid[y][x] < val:
                dp[i][j] = max(dp[i][j], dp[y][x] + 1)

# print(dp)

answer = 0
for row in dp:
    answer = max(answer, max(row))

print(answer)