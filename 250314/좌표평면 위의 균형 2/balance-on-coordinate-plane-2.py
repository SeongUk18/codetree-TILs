n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_point = float('inf')
for x, y in points:
    line_x = x + 1
    line_y = y + 1
    part_1 = 0
    part_2 = 0
    part_3 = 0
    part_4 = 0

    for i in range(len(points)):
        x, y = points[i]

        if x < line_x and y < line_y:
            part_3 += 1
        elif x < line_x and y > line_y:
            part_2 += 1
        elif x > line_x and y < line_y:
            part_4 += 1
        elif x > line_x and y > line_y:
            part_1 += 1
        
    point = max(part_1, part_2, part_3, part_4)

    min_point = min(min_point, point)

print(min_point)
