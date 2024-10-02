# 입력 받기
n, t = map(int, input().split())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

# 주위를 보기 위한 배열
x_list = [-1, -1, 0, 1, 1, 1, 0, -1]
y_list = [0, -1, -1, -1, 0, 1, 1, 1]

# 숫지 미리 위치 저장
position_dict = {}
for i in range(n):
    for j in range(n):
        position_dict[map_list[i][j]] = (i, j)


# 주위 숫자 검색 (숫자 특정 위치 찾기)
for _ in range(t):
    for target in range(1, n * n + 1):
        x, y = position_dict[target]
        # 숫자 위아래 다 보기
        max_num = 0
        next_position = []

        for k in range(len(x_list)):
            cur_x = x + x_list[k]
            cur_y = y + y_list[k]

            # 큰 수 찾기
            if 0 <= cur_x < n and 0 <= cur_y < n and max_num < map_list[cur_x][cur_y]:
                max_num = map_list[cur_x][cur_y]
                next_position = (cur_x, cur_y)

        # 숫자 바꾸기
        map_list[x][y], map_list[next_position[0]][next_position[1]] = map_list[next_position[0]][next_position[1]], map_list[x][y]
        # 위치 정보도 갱신
        position_dict[map_list[x][y]] = (x, y)
        

for i in range(n):
    for j in range(n):
        print(map_list[i][j], end = " ")
    print()