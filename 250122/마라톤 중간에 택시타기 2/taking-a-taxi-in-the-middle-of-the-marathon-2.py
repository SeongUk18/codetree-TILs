n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_dist = float('inf')

for i in range(1, n - 1):
    cur_x = 0
    cur_y = 0
    dist = 0
    for j in range(1, n):
        if j == i:
            continue

        dist += abs(x[cur_x] - x[j]) + abs(y[cur_y] - y[j])
        cur_x = j
        cur_y = j

    min_dist = min(dist, min_dist)


print(min_dist)