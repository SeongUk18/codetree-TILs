n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

area = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        if x[i] == x[j]:
            for k in range(n):
                if k == i or k == j:
                    continue
                else:
                    if y[j] == y[k]:
                        area = abs(x[k] - x[i]) * abs(y[i] - y[k])
                    elif y[i] == y[k]:
                        area = abs(x[k] - x[i]) * abs(y[j] - y[k])

        elif y[i] == y[j]:
            for k in range(n):
                if k == i or k == j:
                    continue
                else:
                    if x[j] == x[k]:
                        area = abs(y[k] - y[i]) * abs(x[i] - x[k])
                    elif x[i] == x[k]:
                        area = abs(y[k] - y[i]) * abs(x[j] - x[k])

print(area)