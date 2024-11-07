# 그리드 크기와 숫자 입력 받기
n, m = map(int, input().split())

map_list = []
for _ in range(n):
    map_list.append(list(map(int, input().split())))

# 블록 모양 정의 (3칸으로 구성된 L 및 I 모양)
tetrominoes = [
    # L-shape
    [(0, 0), (1, 0), (1, 1)],  # 기본 형태
    [(0, 0), (0, 1), (1, 0)],  # 90도 회전
    [(0, 0), (1, 0), (2, 0)],  # 세로형
    [(0, 0), (0, 1), (1, 1)],  # 반전 형태
    
    # I-shape
    [(0, 0), (0, 1), (0, 2)],  # 기본 수평
    [(0, 0), (1, 0), (2, 0)],  # 90도 회전(수직)
]

# 블록을 배치하여 최대 합을 계산하는 함수
def get_max_sum():
    max_sum = 0

    for i in range(n):
        for j in range(m):
            for shape in tetrominoes:
                # 각 모양의 가능한 위치에 대한 합을 계산
                current_sum = 0
                valid = True
                for dx, dy in shape:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        current_sum += map_list[nx][ny]
                    else:
                        valid = False
                        break
                if valid:
                    max_sum = max(max_sum, current_sum)

    return max_sum

# 최대 합 출력
print(get_max_sum())