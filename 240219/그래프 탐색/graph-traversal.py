n, m = map(int, input().split())

node_list = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    node_list[i].append(j)
    node_list[j].append(i)

print(len(node_list[1]))