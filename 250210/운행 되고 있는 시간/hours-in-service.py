n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]


max_time = float('-inf')
for i in range(n):
    time_set = set()
    for j in range(n):
        if i == j:
            continue
        # print(a[j], b[j])
        set_time = set(list(range(a[j], b[j])))
        time_set = time_set.union(set_time)
        # print(time_set)
    max_time = max(len(time_set), max_time)

print(max_time)