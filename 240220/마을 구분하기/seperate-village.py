from collections import deque

n = int(input())

map_list = []
map_chk = [[False for _ in range(n)] for _ in range(n)]
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]
town_list = []
for _ in range(n):
    map_list.append(list(map(int, input().split())))

def bfs(node):
    count = 1
    y, x = node
    q = deque()
    q.append((y, x))
    map_chk[y][x] = True
    while q:
        cur_y, cur_x = q.popleft()
        for i in range(4):
            next_x = cur_x + x_list[i]
            next_y = cur_y + y_list[i]
            if 0 > next_y or 0 > next_x or next_y >= n or next_x >= n or map_list[next_y][next_x] == 0 or map_chk[next_y][next_x]:
                continue
            q.append((next_y, next_x))
            map_chk[next_y][next_x] = True
            count += 1
    return count

for i in range(n):
    for j in range(n):
        if map_list[j][i] == 0 or map_chk[j][i]:
            continue
        town_list.append(bfs((j,i)))

town_list.sort()

print(len(town_list))
for i in town_list:
    print(i)