from collections import deque

# 입력받기
n, m = map(int, input().split())

map_list = []


for _ in range(n):
    map_list.append(list(map(int, input().split())))
 
answer = (0, 0)
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

def bfs(i, j, map_check, k):
    q = deque()
    q.append((i, j))
    map_check[i][j] = True

    while q:
        x, y = q.popleft()

        for a in range(4):
            cur_x = x + x_list[a]
            cur_y = y + y_list[a]

            if 0 <= cur_x < n and 0 <= cur_y < m and not map_check[cur_x][cur_y] and map_list[cur_x][cur_y] > k:
                q.append((cur_x, cur_y))
                map_check[cur_x][cur_y] = True


for k in range(1, 101):
    size = 0
    map_check = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not map_check[i][j] and map_list[i][j] > k:
                bfs(i, j, map_check, k)
                size += 1
    
    if answer[1] < size:
        answer = (k, size)

print(" ".join(map(str, answer)))