from collections import deque

n, m = map(int, input().split())

map_check = [[False for _ in range(m)] for _ in range(n)]

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, -1))
    map_check[0][0] = True

    while q:
        x, y, dist = q.popleft()
        
        # 목표 지점에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist + 1


        for i in range(4):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if 0 <= cur_x < n and 0 <= cur_y < m and map_check[cur_x][cur_y] == False and map_list[cur_x][cur_y] == 1:
                q.append((cur_x, cur_y, dist + 1)) 
                map_check[cur_x][cur_y] = True

    return - 1

answer = bfs()


print(answer)