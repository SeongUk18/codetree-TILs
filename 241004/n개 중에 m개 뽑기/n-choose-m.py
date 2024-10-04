# 입력 받기
n, m = map(int, input().split())

# 수열 생성
num_list = [i for i in range(1, n + 1)]

# 백트래킹
def backtracking(start, answer):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for num in range(start, n + 1):
        answer.append(num)
        backtracking(num + 1, answer)
        answer.pop()

backtracking(1, [])