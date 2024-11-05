n, m = map(int, input().split())

num_list = []
for _ in range(n):
    num_list.append(list(map(int, input().split())))

answer = 0

# 가로 확인
for i in range(n):
    prev_num = num_list[i][0]
    count = 1
    found = False  # 중복 카운트 방지용 변수 추가
    for j in range(1, n):
        if num_list[i][j] == prev_num:
            count += 1
        else:
            if count >= m:
                answer += 1
                found = True
                break
            prev_num = num_list[i][j]
            count = 1
    if count >= m and not found:  # 마지막 구간 검사
        answer += 1

# 세로 확인
for i in range(n):
    prev_num = num_list[0][i]
    count = 1
    found = False  # 중복 카운트 방지용 변수 추가
    for j in range(1, n):
        if num_list[j][i] == prev_num:
            count += 1
        else:
            if count >= m:
                answer += 1
                found = True
                break
            prev_num = num_list[j][i]
            count = 1
    if count >= m and not found:  # 마지막 구간 검사
        answer += 1

print(answer)