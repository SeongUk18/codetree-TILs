# 입력값 받기
n, m, k = map(int, input().split())

space = []

for _ in range(n):
    space.append(list(map(int, input().split())))

check = True
# 맵 맨 아래줄부터 m, k 가 들어갈 수 있는지 확인
for i in range(1, n):
    if all(space[i][j] == 0 for j in range(k - 1, k - 1 + m)):
        for j in range(k - 1, k - 1 + m):
            space[i][j] = 1
            check = False
        break

if check:
    for j in range(k - 1, k - 1 + m):
        space[0][j] = 1

for i in range(n):
    for j in range(n):
        print(space[i][j], end=" ")
    print()