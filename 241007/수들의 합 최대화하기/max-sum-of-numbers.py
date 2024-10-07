# 입력 받기
n = int(input())

# 표 생성
num_list = []
for _ in range(n):
    num_list.append(list(map(int, input().split())))

# 색칠 가능 여부 확인용 list
locate_list = [[False for _ in range(n)] for _ in range(n)]

# 색칠할 수 있는지 확인
def is_vaild(row, col, locate_list):
    # 같은 열에 1개인지 확인
    for i in range(row):
        if locate_list[i][col]:
            return False
    
    # 같은 열에 1개인지 확인
    for i in range(col):
        if locate_list[row][i]:
            return False

    return True

# 백트래킹용 함수
def backtracking(answer_list, row, n, answer):
    # 총 갯수가 n개라면 다 놓인 거니 리턴
    if row == n:
        # 결과 값들을 다 저장
        answer_list.append(answer)
        return

    for col in range(n):
        if is_vaild(row, col, locate_list):
            locate_list[row][col] = True
            answer += num_list[row][col]
            # 재귀 호출
            backtracking(answer_list, row + 1, n, answer)
            # 백트래킹
            locate_list[row][col] = False
            answer -= num_list[row][col]


answer_list = []
backtracking(answer_list, 0, n, 0)

print(max(answer_list))