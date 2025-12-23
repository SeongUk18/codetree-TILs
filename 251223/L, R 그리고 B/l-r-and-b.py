from collections import deque

board = [list(input()) for _ in range(10)]

# Please write your code here.
checked = [[False for _ in range(10)] for _ in range(10)]
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

answer = float('inf')
q = deque()

def bfs():
    global answer
    while q:
        # print(q)
        x, y, dist = q.popleft()

        for i in range(4):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if cur_x < 10 and cur_y < 10 and checked[cur_x][cur_y] == False:
                if board[cur_x][cur_y] == ".":
                    q.append((cur_x, cur_y, dist + 1))
                    checked[cur_x][cur_y] = True
                elif board[cur_x][cur_y] == "B":
                    answer = min(answer, dist)

for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            q.append((i, j, 0))
            checked[i][j] = True
            bfs()

print(answer)