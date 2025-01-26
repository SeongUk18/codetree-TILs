N, M = map(int, input().split())
arr = [input() for _ in range(N)]

x_list = [-1, -1, 0, 1, 1, 1, 0, -1]
y_list = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            for k in range(8):
                x = i + x_list[k]
                y = j + y_list[k]

                if 0 <= x < N and 0 <= y < M and arr[x][y] == "E":
                    x += x_list[k]
                    y += y_list[k]
                    
                    if 0 <= x < N and 0 <= y < M and arr[x][y] == "E":
                        answer += 1


print(answer)