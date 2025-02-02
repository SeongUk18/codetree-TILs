N = int(input())
people = []

for _ in range(N):
    pos, ch = input().split()
    people.append((int(pos), ch))

people.sort()

max_size = 0

for i in range(N):
    g_count = 0
    h_count = 0
    for j in range(i, N):
        if people[j][1] == 'G':
            g_count += 1
        else:
            h_count += 1
        
        if g_count == h_count:
            max_size = max(max_size, people[j][0] - people[i][0])

print(max_size)
