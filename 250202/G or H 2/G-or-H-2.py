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

if types.count('H') == 0:
    max_size = max(max_size, positions[-1] - positions[0])

if types.count('G') == 0:
    max_size = max(max_size, positions[-1] - positions[0])

print(max_size)
