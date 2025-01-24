board = [list(map(int, input().split())) for _ in range(19)]

def sol():
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            
            color = board[i][j]
            cnt = 0
            for k in range(5):
                if j + 4 < 19 and color == board[i][j + k]:
                    cnt += 1

                if cnt == 5:
                    print(color)
                    print(i + 1, j + k - 1)
                    return

            cnt = 0
            for k in range(5):
                if i + 4 < 19 and color == board[i + k][j]:
                    cnt += 1

                if cnt == 5:
                    print(color)
                    print(i + k - 1, j + 1)
                    return

            cnt = 0
            for k in range(5):
                if i + 4 < 19 and j + 4 < 19 and color == board[i + k][j + k]:
                    cnt += 1

                if cnt == 5:
                    print(color)
                    print(i + k - 1, j + k - 1)
                    return

            cnt = 0
            for k in range(5):
                if i >= 4 and j + 4 < 19 and  color == board[i - k][j + k]:
                    cnt += 1

                if cnt == 5:
                    print(color)
                    print(i - 1, j + k - 1)
                    return
    print(0)

sol()