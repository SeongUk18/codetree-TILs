N = int(input())
heights = [int(input()) for _ in range(N)]

min_cost = float('inf')
for i in range(1, 101 - 17):
    mx_h = i + 17
    cost = 0
    for h in heights:
        if h < i:
            cost += (i - h) * (i - h)
        elif h > mx_h:
            cost += (mx_h - h) * (mx_h - h)

    min_cost = min(min_cost, cost)

print(min_cost)