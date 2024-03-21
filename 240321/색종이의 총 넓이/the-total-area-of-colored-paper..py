n = int(input())

map_list = [[0 for _ in range(201)] for _ in range(201)]
answer = 0

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(8):
        for j in range(8):
            if map_list[i + y][j + x] == 1:
                continue
            else:
                map_list[i + y][j + x] = 1
    
for result in map_list:
    answer += sum(result)

print(answer)