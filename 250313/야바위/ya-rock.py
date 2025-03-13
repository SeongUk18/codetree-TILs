n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
max_point = float('-inf')


for i in range(1, 4):
    stone_list = [1 if x == i else 0 for x in range(4)]
    # print(stone_list)
    point = 0
    for a, b, c in moves:
        stone_list[a], stone_list[b] = stone_list[b], stone_list[a]

        if stone_list[c] == 1:
            point += 1
    
    max_point = max(point, max_point)


print(max_point)
    
