from collections import deque

n, m = map(int, input().split())

node_list = [[] for _ in range(n + 1)]
node_chk = [False for _ in range(n + 1)]


for _ in range(m):
    i, j = map(int, input().split())
    node_list[i].append(j)
    node_list[j].append(i)

def bfs(node):
    q = deque()
    q.append(node)
    answer = 0
    while q:
        node = q.popleft()
        node_chk[node] = True
        for k in node_list[node]:
            if not node_chk[k]:
                q.append(k)
                node_chk[k] = True
                answer += 1
    return answer

answer = bfs(1)

print(answer)