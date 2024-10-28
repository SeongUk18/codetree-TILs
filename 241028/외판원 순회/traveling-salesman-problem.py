n = int(input())

visited = [False for _ in range(n + 1)]

node_list = []

for _ in range(n):
    node_list.append(list(map(int, input().split())))

min_cost = float('inf')
visited[0] = True

def dfs(count, cur, cur_cost):
    global min_cost

    if count == n and node_list[cur][0] != 0:
        min_cost = min(min_cost, cur_cost + node_list[cur][0])
        return 

    if cur_cost >= min_cost:
        return

    for i in range(n):
        if visited[i] == False and node_list[cur][i] != 0:
            visited[i] = True
            dfs(count + 1, i, cur_cost + node_list[cur][i])
            visited[i] = False


dfs(1, 0, 0)
print(min_cost)