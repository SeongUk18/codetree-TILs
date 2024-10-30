from collections import deque

n, h, m = map(int, input().split())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]


def bfs(i, j, n):
    q = deque()
    q.append((i, j, 0))
    visited[i][j] = True

    while q:
        x, y, dist = q.popleft()

        if map_list[x][y] == 3:
            return dist

        for i in range(4):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if 0 <= cur_x < n and 0 <= cur_y < n and visited[cur_x][cur_y] == False and map_list[cur_x][cur_y] != 1:
                q.append((cur_x, cur_y, dist + 1))
                visited[cur_x][cur_y] = True

    return -1

answer_list = []

for i in range(n):
    answer = []
    for j in range(n):
        if map_list[i][j] == 2:
            visited = [[False for _ in range(n)] for _ in range(n)]
            answer.append(bfs(i, j, n))
        else:
            answer.append(0)

    answer_list.append(answer)


for i in answer_list:
    for j in i:
        print(j, end=" ")
    print()