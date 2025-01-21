n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = []

def backtracking(cur_x, cur_y, n, road, dist):
    if road == n - 3:
        answer.append(dist + abs(cur_x - x[-1]) + abs(cur_y - y[-1]))
        return
    elif road > n - 3:
        return

    for i, j in points[1: -1]:
        backtracking(i, j, n, road + 1, dist + abs(cur_x - i) + abs(cur_y - j))
        
backtracking(x[0], y[0], n, 0, 0)


print(min(answer))
