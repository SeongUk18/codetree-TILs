from collections import deque

n, m = map(int, input().split())

map_chk = [[False for _ in range(m)] for _ in range(n)]
map_list = []
change_y = [1, 0]
change_x = [0, 1]

for _ in range(n):
    map_list.append(list(map(int, input().split())))

def bfs(node):
    x, y = node
    q = deque()
    q.append((y, x))
    map_chk[y][x] = True
    while q:
        cur_y, cur_x = q.popleft()
        for i in range(2):
            next_y = cur_y + change_y[i]
            next_x = cur_x + change_x[i]
            if next_y >= n or next_x >= m or not map_chk[next_y][next_x] or map_list[next_y][next_x] == 0:
                continue
            elif next_x == (n - 1) and next_y == (m - 1):
                return 1
            else:
                q.append((next_y,next_x))
                map_chk[next_y][next_y] = True
    return 0

print(bfs((0, 0)))