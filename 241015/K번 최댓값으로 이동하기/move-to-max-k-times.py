# 입력값을 처리하고 문제 해결을 위한 함수를 작성
def find_final_position(n, k, grid, start_r, start_c):
    # 상하좌우 이동을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위, 아래, 왼쪽, 오른쪽 순
    
    # 현재 위치를 0-indexed로 변경
    r, c = start_r - 1, start_c - 1

    # k번 반복하거나 더 이상 이동할 곳이 없을 때까지 반복
    for _ in range(k):
        current_value = grid[r][c]
        candidates = []

        # 상하좌우 탐색
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbor_value = grid[nr][nc]
                if neighbor_value < current_value:
                    candidates.append((neighbor_value, nr, nc))
        
        # 이동할 수 있는 후보가 없으면 종료
        if not candidates:
            break

        # 후보 중 가장 큰 값으로 이동 (우선순위: 값 -> 행 -> 열)
        candidates.sort(key=lambda x: (-x[0], x[1], x[2]))  # 값은 내림차순, 행과 열은 오름차순
        _, r, c = candidates[0]  # 첫 번째 후보로 이동

    # 최종 위치 반환
    return r, c

# 입력 예시를 기반으로 동작 확인
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_r, start_c = map(int, input().split())

# 결과 출력
final_r, final_c = find_final_position(n, k, grid, start_r, start_c)
print(final_r, final_c)