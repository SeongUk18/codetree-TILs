n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
x_list = [-1, -1, 1, 1] 
y_list = [1, -1, -1, 1]

def check(r, c):
    cur_x, cur_y = r, c
    total_sum = 0

    for i in range(4):
        for _ in range(move_distances[i]):
            cur_x += x_list[i]
            cur_y += y_list[i]
            
            if not (0 <= cur_x < n and 0 <= cur_y < n):
                return 0             
            
            total_sum += grid[cur_x][cur_y]

    return total_sum

for r in range(n):
    for c in range(n):
        for w in range(1, n):
            for h in range(1, n):
                move_distances = [w, h, w, h]
                answer = max(answer, check(r, c))

print(answer)
