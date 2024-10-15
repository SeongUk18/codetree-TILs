from collections import deque

def bfs(n, grid, start_r, start_c):
    # 상하좌우 이동을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위, 아래, 왼쪽, 오른쪽 순
    
    queue = deque([(start_r, start_c)])
    visited = [[False] * n for _ in range(n)]
    visited[start_r][start_c] = True
    current_value = grid[start_r][start_c]
    reachable_positions = []  # 탐색 가능한 위치들

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                neighbor_value = grid[nr][nc]
                if neighbor_value < current_value:  # 현재 값보다 작은 값만 이동 가능
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    reachable_positions.append((neighbor_value, nr, nc))

    # 가능한 위치들 중 값이 큰 순 -> 행이 작은 순 -> 열이 작은 순으로 정렬
    if reachable_positions:
        reachable_positions.sort(key=lambda x: (-x[0], x[1], x[2]))
        return reachable_positions[0][1], reachable_positions[0][2]  # (r, c) 반환
    else:
        return start_r, start_c  # 더 이상 이동할 수 없으면 제자리

# input 형식으로 받는 부분
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_r, start_c = map(int, input().split())

# 0-indexed로 변환
r, c = start_r - 1, start_c - 1

# k번 이동 반복
for _ in range(k):
    new_r, new_c = bfs(n, grid, r, c)
    if (new_r, new_c) == (r, c):  # 더 이상 이동할 곳이 없으면 종료
        break
    r, c = new_r, new_c

# 최종 위치를 1-indexed로 출력
print(r + 1, c + 1)