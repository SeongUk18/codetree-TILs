n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

visited = [False for _ in range(n)]
min_dist = float('inf')

def backtracking(cur_x, cur_y, n, road, dist):
    global min_dist

    if dist >= min_dist or road > n - 3:
        return

    if road == n - 3:
        dist = dist + abs(cur_x - x[-1]) + abs(cur_y - y[-1])
        min_dist = min(dist, min_dist)
        return 

    for idx in range(1, n - 1):
        visited[idx] = True
        backtracking(x[idx], y[idx], n, road + 1, dist + abs(cur_x - x[idx]) + abs(cur_y - y[idx]))
        visited[idx] = False

visited[0] = True
backtracking(x[0], y[0], n, 0, 0)


print(min_dist)
