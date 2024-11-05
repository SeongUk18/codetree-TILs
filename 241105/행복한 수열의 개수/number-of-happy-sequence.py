n, m = map(int, input().split())

num_list = []
for _ in range(n):
    num_list.append(list(map(int, input().split())))

answer = 0

# 가로 확인
for i in range(n):
    prev_num = num_list[i][0]
    count = 1
    for j in range(1, n):
        if prev_num == num_list[i][j]:
            count += 1
        else:
            prev_num = num_list[i][j]
            count = 1

    if count >= m:
        answer += 1

# 세로 확인
for i in range(n):
    prev_num = num_list[0][i]
    count = 1
    for j in range(1, n):
        if prev_num == num_list[j][i]:
            count += 1
        else:
            prev_num = num_list[j][i]
            count = 1

    if count >= m:
        answer += 1

print(answer)