from collections import deque

# 입력 받기
n, k = map(int, input().split())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

r, c = map(int, input().split())
r -= 1
c -= 1  # 값 보정

next_idx = (r, c)
for _ in range(k):
    x = next_idx[0]
    y = next_idx[1]
    target = float('-inf')
    for i in range(n):
        for j in range(n):
            if map_list[i][j] < map_list[x][y] and target < map_list[i][j]:
                target = map_list[i][j]
                next_idx = (i, j)

    if next_idx[0] == x and next_idx[1] == y:
        break

        

for i in next_idx:
    print(i, end=" ")