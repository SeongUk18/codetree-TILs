plane = [[0 for _ in range(2001)] for _ in range(2001)]
answer = 0

for k in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    if k == 2:
        for i in range(y1 + 1000, y2 + 1000):
            for j in range(x1 + 1000, x2 + 1000):
                plane[i][j] = 0
    else:
        for i in range(y1 + 1000, y2 + 1000):
            for j in range(x1 + 1000, x2 + 1000):
                plane[i][j] = 1

for size in plane:
    answer += sum(size)

print(answer)