from collections import deque

n, m = map(int, input().split())

map_list = []
map_check = [[True for _ in range(m)] for _ in range(n)]
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]
q = deque()

for _ in range(n):
    map_list.append(list(map(int, input().split())))

q.append((0, 0))
map_check[0][0] = False

while q:
    cur_x, cur_y = q.popleft()
    for i in range(4):
        n_x = cur_x + x_list[i]
        n_y = cur_y + y_list[i]
        if 0 <= n_x < m and 0 <= n_y < n and map_check[n_y][n_x] and map_list[n_y][n_x] == 1:
            q.append((n_x, n_y))
            map_check[n_y][n_x] = False

if map_check[n - 1][m - 1]:
    print(0)
else:
    print(1)