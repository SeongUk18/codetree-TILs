n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_area = float('inf')

for i in range(n):
        
    x_list = [x[k] for k in range(n) if k != i]
    y_list = [y[k] for k in range(n) if k != i]
    # print(x_list, y_list)
    if x_list[0] * n - 1 == sum(x_list) or y_list[0] * n - 1 == sum(y_list):
        area = 0
    else:
        area = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))

    min_area = min(area, min_area)

print(min_area)