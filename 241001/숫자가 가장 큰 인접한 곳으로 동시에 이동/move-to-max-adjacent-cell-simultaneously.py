from collections import defaultdict

# 입력 받기
n, m, t = map(int, input().split())

bead = defaultdict(list)

map_list = []
for _ in range(n):
    map_list.append(list(map(int, input().split())))

for i in range(m):
    r, c = map(int, input().split())
    bead[i].append([r - 1, c - 1]) # 좌표값이 1부터 시작해서 -1 추가

# 상하좌우 확인용
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]


for _ in range(t):
    bead_copy = dict(bead)
    for key, locate in bead_copy.items():
        if not locate:
            continue
        x, y = locate[-1]
        max_num = 0
        next_locate = []
        for k in range(4):
            cur_x = x + x_list[k]
            cur_y = y + y_list[k]
            if 0 <= cur_x < n and 0 <= cur_y < n:
                if max_num < map_list[cur_y][cur_x]:
                    max_num = map_list[cur_y][cur_x]
                    next_locate = [cur_x, cur_y]
        # 왔다 갔는지 확인
        if next_locate in locate:
            del bead[key]
        else:
            bead[key].append(next_locate)
                
print(len(bead))