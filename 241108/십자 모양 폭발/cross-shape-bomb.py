n = int(input())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

r, c = map(int, input().split())
r -= 1
c -= 1

def explode_and_apply_gravity(grid, x, y):
    n = len(grid)
    power = grid[x][y]
    
    # Step 1: 폭탄 폭발
    for i in range(-power + 1, power):
        if 0 <= x + i < n:
            grid[x + i][y] = 0  # 상하 폭발
        if 0 <= y + i < n:
            grid[x][y + i] = 0  # 좌우 폭발
    
    # Step 2: 중력 적용
    for col in range(n):
        empty_row = n - 1
        for row in range(n - 1, -1, -1):
            if grid[row][col] != 0:
                grid[empty_row][col] = grid[row][col]
                if empty_row != row:
                    grid[row][col] = 0
                empty_row -= 1
    
    return grid

result_grid = explode_and_apply_gravity(map_list, r, c)
for row in result_grid:
    for i in row:
        print(i, end=" ")
    print()