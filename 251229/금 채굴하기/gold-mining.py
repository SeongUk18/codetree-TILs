from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

q = deque()
answer = 0

def bfs(n, max_dist):
    map_list = [[False for _ in range(n)] for _ in range(n)]

    while q:
        x, y, dist, count = q.popleft()

        if dist > max_dist:
            break

        for i in range(4):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if 0 <= cur_x < n and 0 <= cur_y < n and map_list[cur_x][cur_y] == False:
                if grid[cur_x][cur_y] == 1:
                    count += 1

                q.append((cur_x, cur_y, dist + 1, count))
                map_list[cur_x][cur_y] = True

    return count

def price(k):
    return k * k + (k + 1) * (k + 1)


for i in range(n):
    for j in range(n):
        for k in range(m):
            if grid[i][j] == 1:
                q.append((i, j, 0, 1))
                map_list[i][j] = True
                count = bfs(n, k + 1)
            else:
                q.append((i, j, 0, 0))
                map_list[i][j] = True
                count = bfs(n, k + 1)

        if price(k) <= count * m:
            answer = max(answer, count)


print(answer)