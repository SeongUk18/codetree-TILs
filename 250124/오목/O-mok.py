board = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        
        color = board[i][j]
        cnt = 0
        for k in range(5):
            if color == board[i][j + k]:
                cnt += 1

            if cnt == 5:
                print(color)
                print(i + 1, j + k - 1)
                break

        cnt = 0
        for k in range(5):
            if color == board[i + k][j]:
                cnt += 1

            if cnt == 5:
                print(color)
                print(i + k - 1, j + 1)
                break

        cnt = 0
        for k in range(5):
            if color == board[i + k][j + k]:
                cnt += 1

            if cnt == 5:
                print(color)
                print(i + k - 1, j + k - 1)
                break

        cnt = 0
        for k in range(5):
            if if i >=4 and color == board[i - k][j + k]:
                cnt += 1

            if cnt == 5:
                print(color)
                print(i + 2, j + k - 1)
                break