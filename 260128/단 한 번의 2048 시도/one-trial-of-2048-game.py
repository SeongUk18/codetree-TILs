# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
if dir == "L":
    for k in range(4):
        start = 0
        while start <= 3:    
            for i in range(start + 1, 4):
                if grid[k][i] == 0:
                    continue
                    
                if grid[k][i] == grid[k][start]:
                    grid[k][start] *= 2
                    grid[k][i] = 0
                    break
                else:
                    break

            start += 1
    for k in range(4):
        for i in range(4):
            if grid[k][i] == 0:
                start = i
                for j in range(i, 4):
                    if grid[k][j] != 0:
                        grid[k][i], grid[k][j] = grid[k][j], grid[k][i]
                        break
                    
        

if dir == "R":
    for k in range(4):
        start = 3
        while start >= 0:    
            for i in range(start - 1, -1, -1):
                if grid[k][i] == 0:
                    continue
                    
                if grid[k][i] == grid[k][start]:
                    grid[k][start] *= 2
                    grid[k][i] = 0
                    break
                else:
                    break

            start -= 1
    for k in range(4):
        for i in range(3, -1, -1):
            if grid[k][i] == 0:
                start = i
                for j in range(i, -1, -1):
                    if grid[k][j] != 0:
                        grid[k][i], grid[k][j] = grid[k][j], grid[k][i]
                        break

if dir == "D":
    for k in range(4):
        start = 3
        while start >= 0:    
            for i in range(start - 1, -1, -1):
                if grid[i][k] == 0:
                    continue
                    
                if grid[i][k] == grid[start][k]:
                    grid[start][k] *= 2
                    grid[i][k] = 0
                    break
                else:
                    break

            start -= 1

    for k in range(4):
        for i in range(3, -1, -1):
            if grid[i][k] == 0:
                start = i
                for j in range(i, -1, -1):
                    if grid[j][k] != 0:
                        grid[i][k], grid[j][k] = grid[j][k], grid[i][k]
                        break
if dir == "U":
    for k in range(4):
        start = 0
        while start <= 3:    
            for i in range(start + 1, 4):
                if grid[i][k] == 0:
                    continue
                    
                if grid[i][k] == grid[start][k]:
                    grid[start][k] *= 2
                    grid[i][k] = 0
                    break
                else:
                    break

            start += 1
    for k in range(4):
        for i in range(4):
            if grid[i][k] == 0:
                start = i
                for j in range(i, 4):
                    if grid[j][k] != 0:
                        grid[i][k], grid[j][k] = grid[j][k], grid[i][k]
                        break





for i in range(4):
    for j in range(4):
        print(grid[i][j], end=" ")
    print()