n = int(input())

plane = [[0 for _ in range(201)] for _ in range(201)]
answer = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1 + 100, y2 + 100):
        for j in range(x1 + 100, x2 + 100):
            plane[i][j] = 1

for size in plane:
    answer += sum(size)

print(answer)