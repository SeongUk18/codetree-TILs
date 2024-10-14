from collections import deque

# 입력 받기
n = int(input())

start_x, start_y, end_x, end_y = map(int, input().split())
start_x -= 1
start_y -= 1
end_x -= 1
end_y -= 1

map_list = [[False for _ in range(n)] for _ in range(n)]

# 나이트 움직일 수 있는 곳 계산
x_list = [-2, -1, 1, 2, 2, 1, -1, -2]
y_list = [-1, -2, -2, -1, 1, 2, 2, 1]

# 탐색
def bfs(start_x, start_y, end_x, end_y, n):
    q = deque()
    q.append((start_x, start_y, 0))
    map_list[start_x][start_y] = True

    while q:
        x, y, dist = q.popleft()

        if x == end_x and y == end_y:
            return dist

        for i in range(len(x_list)):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if 0 <= cur_x < n and 0 <= cur_y < n and map_list[cur_x][cur_y] == False:
                q.append((cur_x, cur_y, dist + 1))
                map_list[cur_x][cur_y] = True

    return -1


answer = bfs(start_x, start_y, end_x, end_y, n)

print(answer)