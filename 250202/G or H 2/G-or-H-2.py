N = int(input())
people = [tuple(input().split()) for _ in range(N)]
people = sorted((int(pos), ch) for pos, ch in people)

positions = [pos for pos, ch in people]  
types = [ch for pos, ch in people] 

max_size = 0

for i in range(N):
    g_count = h_count = 0
    for j in range(i, N):
        if types[j] == 'G':
            g_count += 1
        else:
            h_count += 1
        if g_count == h_count:  
            max_size = max(max_size, positions[j] - positions[i])

max_g_run = 0
start = None
for i in range(N):
    if types[i] == 'G':
        if start is None:
            start = positions[i]
        max_g_run = max(max_g_run, positions[i] - start)
    else:
        start = None

max_h_run = 0
start = None
for i in range(N):
    if types[i] == 'H':
        if start is None:
            start = positions[i]
        max_h_run = max(max_h_run, positions[i] - start)
    else:
        start = None

max_size = max(max_size, max_g_run, max_h_run)
print(max_size)
