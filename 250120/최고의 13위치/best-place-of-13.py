n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(n):

        coin = 0
        for k in range(3):
            if k + j < n:
                if grid[i][k + j] == 1:
                    coin += 1
        answer = max(answer, coin)

        coin = 0
        for k in range(3):
            if k + i < n:
                if grid[k + i][j] == 1:
                    coin += 1
        answer = max(answer, coin)


print(answer)