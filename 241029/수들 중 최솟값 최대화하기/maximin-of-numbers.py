n = int(input())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

def is_valid_choice(matrix, n, threshold, row_visited, col_visited, row):
    # 모든 행에 대해 조건에 맞게 선택 가능한지 확인
    if row == n:
        return True
    
    for col in range(n):
        # 이미 방문한 열이거나 현재 칸의 값이 임계값 미만일 경우 스킵
        if col_visited[col] or matrix[row][col] < threshold:
            continue
        
        # 현재 열을 선택하고 다음 행으로 이동
        col_visited[col] = True
        if is_valid_choice(matrix, n, threshold, row_visited, col_visited, row + 1):
            return True
        col_visited[col] = False  # 백트래킹
        
    return False

def max_min_value(matrix, n):
    # 가능한 값의 범위 설정
    low, high = 0, max(map(max, matrix))
    answer = 0
    
    while low <= high:
        mid = (low + high) // 2
        # 현재 임계값으로 색칠할 수 있는지 확인
        row_visited = [False] * n
        col_visited = [False] * n
        
        if is_valid_choice(matrix, n, mid, row_visited, col_visited, 0):
            answer = mid  # 가능한 경우 답을 갱신하고 더 큰 값 탐색
            low = mid + 1
        else:
            high = mid - 1  # 불가능한 경우 더 작은 값 탐색
    
    return answer

print(max_min_value(map_list, n))