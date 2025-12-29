from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

q = deque()
answer = 0

def bfs(n, max_dist, gold):
    total_gold = gold
    while q:
        x, y, dist = q.popleft()
        # print(x, y, dist, count)

        for i in range(4):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if 0 <= cur_x < n and 0 <= cur_y < n and map_list[cur_x][cur_y] == False and dist + 1 <= max_dist:
                if grid[cur_x][cur_y] == 1:
                    total_gold += 1

                q.append((cur_x, cur_y, dist + 1))
                map_list[cur_x][cur_y] = True

    return total_gold

def price(k):
    return k * k + (k + 1) * (k + 1)


for i in range(n):
    for j in range(n):
        for k in range(n):
            map_list = [[False for _ in range(n)] for _ in range(n)]
            if grid[i][j] == 1:
                q.append((i, j, 0))
                map_list[i][j] = True
                count = bfs(n, k, 1)
            else:
                q.append((i, j, 0))
                map_list[i][j] = True
                count = bfs(n, k, 0)

            if price(k) <= count * m:
                answer = max(answer, count)


print(answer)