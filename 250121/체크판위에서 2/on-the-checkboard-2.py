R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]


start_idx = (0, 0)
start_color = grid[0][0]

end_idx = (R - 1, C - 1)
end_color = grid[R - 1][C - 1]


next_idx = []

for i in range(1, R):
    for j in range(1, C):
        if grid[i][j] != start_color:
            next_idx.append((i, j))

next_idx2 = []
for x, y in next_idx:
    for i in range(x + 1, R):
        for j in range(y + 1, C):
            if grid[x][y] != grid[i][j]:
                next_idx2.append((i, j))

answer = 0
for x, y in next_idx2:
    if x + 1 < R and y + 1 < C and grid[x][y] != end_color:
        answer += 1

print(answer)