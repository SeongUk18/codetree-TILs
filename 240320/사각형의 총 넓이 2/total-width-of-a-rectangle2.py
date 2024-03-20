n = int(input())

plane = [[0 for _ in range(100)] for _ in range(100)]
answer = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            plane[i][j] = 1

for size in plane:
    answer += sum(size)

print(answer)