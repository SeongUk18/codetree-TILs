map_list = [[0 for _ in range(2001)] for _ in range(2001)]

x1, y1, x2, y2 = map(int, input().split())

for i in range(y2 - y1 + 1):
    for j in range(x2 - x1 + 1):
        map_list[y1 + i][x1 + j] = 1

x1, y1, x2, y2 = map(int, input().split())

for i in range(y2 - y1):
    for j in range(x2 - x1):
        map_list[y1 + i][x1 + j] = 0

answer_x = []
answer_y = []
for i in range(len(map_list)):
    for j in range(len(map_list[i])):
        if map_list[i][j] != 1:
            continue
        else:
            answer_x.append(j)
            answer_y.append(i)
# print(answer_x, answer_y)
max_x = max(answer_x)
min_x = min(answer_x)
min_y = min(answer_y)
max_y = max(answer_y)

print((max_x - min_x) * (max_y - min_y))