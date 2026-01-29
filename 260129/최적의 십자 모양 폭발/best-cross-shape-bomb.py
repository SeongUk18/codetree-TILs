n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = float('-inf')

def boom(i, j):
    new_grid = [a[:] for a in grid]

    for k in range(grid[i][j]):
        if i - k >= 0: 
            new_grid[i - k][j] = 0
        if k + i < n:
            new_grid[k + i][j] = 0
        if j - k >= 0:
            new_grid[i][j - k] = 0
        if k + j < n:
            new_grid[i][k + j] = 0

    return new_grid

def gravity(new_gird):
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if new_grid[i][j] == 0:
                k = 1
                while i - k >= 0:
                    if new_gird[i - k][j] != 0:
                        new_grid[i][j], new_grid[i - k][j] = new_grid[i - k][j], new_grid[i][j]
                        break
                    k += 1

    return new_grid


def count_num(new_grid_gravity):
    count = 0
    for i in range(n):
        for j in range(n):
            if new_grid_gravity[i][j] == 0:
                continue
            if j + 1 < n and new_grid_gravity[i][j] == new_grid_gravity[i][j + 1]:
                count += 1
            if i + 1 < n and new_grid_gravity[i + 1][j] == new_grid_gravity[i][j]:
                count += 1
    return count

for i in range(n):
    for j in range(n):
        new_grid = boom(i, j)
        new_grid_gravity = gravity(new_grid)
        answer = max(count_num(new_grid_gravity), answer)

print(answer)