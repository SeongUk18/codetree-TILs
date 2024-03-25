n = int(input())

map_list = [[0 for _ in range(201)] for _ in range(201)]

for k in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    if k % 2 == 0:
        for i in range(1, y2 - y1 + 1):
            for j in range(1, x2 - x1 + 1):
                map_list[y1 + i][x1 + j] = 0
    else:
        for i in range(1, y2 - y1 + 1):
            for j in range(1, x2 - x1 + 1):
                map_list[y1 + i][x1 + j] = 1

answer = 0

for i in map_list:
    answer += sum(i)
print(answer)