from collections import deque

n = int(input())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

map_check = [[False for _ in range(n)] for _ in range(n)]

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

def bfs(i, j, num):
    q = deque()
    q.append((i, j))
    map_check[i][j] = True
    size = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if 0 <= cur_x < n and 0 <= cur_y < n and map_list[cur_x][cur_y] == num and map_check[cur_x][cur_y] == False:
                q.append((cur_x, cur_y))
                map_check[cur_x][cur_y] = True
                size += 1
        # print(q)
    return size


count = 0
answer = 0

for i in range(n):
    for j in range(n):
        if map_check[i][j] == False:
            size = bfs(i, j, map_list[i][j])
            if size >= 4:
                count += 1
            answer = max(answer, size)

print(count, answer)