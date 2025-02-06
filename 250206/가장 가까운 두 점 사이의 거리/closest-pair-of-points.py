n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_dist = float('inf')
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dist = pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2)
        min_dist = min(abs(dist), min_dist)

print(min_dist)