# 입력값 받기
n, m, k = map(int, input().split())

space = []

for _ in range(n):
    space.append(list(map(int, input().split())))


# 맵 맨 아래줄부터 m, k 가 들어갈 수 있는지 확인
for i in range(n - 1, -1, -1):
    if all(space[i][j] == 0 for j in range(k - 1, k - 1 + m)) and all(sum(space[z][k - 1: k + m - 1]) == 0 for z in range(i)):
        # 맨 아랫줄부터 안채워져 있을 수 있으니 확인 필요
        for j in range(k - 1, k - 1 + m):
            space[i][j] = 1
        break

for i in range(n):
    for j in range(n):
        print(space[i][j], end=" ")
    print()