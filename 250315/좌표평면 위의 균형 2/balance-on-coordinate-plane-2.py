n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_point = float('inf')
for line_x in range(0, 101, 2):
    for line_y in range(0, 101, 2):

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
    # print(point, line_x, line_y)
        min_point = min(min_point, point)

print(min_point)
