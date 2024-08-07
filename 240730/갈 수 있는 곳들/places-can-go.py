from collections import deque

n, k = map(int, input().split())

map_list = []
map_check = [[True for _ in range(n)] for _ in range(n)]
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]
q = deque()
count = 0

for _ in range(n):
    map_list.append(list(map(int, input().split())))

for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    if map_check[r][c]:
        q.append((r, c))
        map_check[r][c] = False
        count += 1

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + x_list[i]
            ny = cur_y + y_list[i]

            if 0 <= nx < n and 0 <= ny < n and map_check[nx][ny] and map_list[nx][ny] == 0:
                q.append((nx, ny))
                map_check[nx][ny] = False
                count += 1

print(count)