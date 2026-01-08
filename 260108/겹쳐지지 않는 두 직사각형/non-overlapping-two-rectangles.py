n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 모든 가능한 직사각형을 담을 리스트
rects = []

# (r1, c1)은 직사각형의 왼쪽 위, (r2, c2)는 오른쪽 아래 좌표
for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                # 직사각형 내부의 숫자 합 계산
                current_sum = 0
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        current_sum += grid[i][j]
                
                # (좌표 정보, 합계)를 리스트에 저장
                rects.append(((r1, c1, r2, c2), current_sum))

# 두 직사각형이 겹치는지 확인하는 함수
def is_overlapping(rect1, rect2):
    (r1, c1, r2, c2) = rect1
    (R1, C1, R2, C2) = rect2
    
    # 한 직사각형의 행 범위가 다른 쪽과 겹치고, 동시에 열 범위도 겹치면 겹치는 것임
    if r1 <= R2 and R1 <= r2 and c1 <= C2 and C1 <= c2:
        return True
    return False

max_sum = -float('inf') 

num_rects = len(rects)
for i in range(num_rects):
    for j in range(i + 1, num_rects):
        rect1_coords, sum1 = rects[i]
        rect2_coords, sum2 = rects[j]
        
        # 겹치지 않을 때만 최댓값 확인
        if not is_overlapping(rect1_coords, rect2_coords):
            max_sum = max(max_sum, sum1 + sum2)

print(max_sum)