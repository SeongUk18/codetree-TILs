from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()

visited = [float('inf') for _ in range(n)]
visited[0] = arr[0]
q.append((0, arr[0]))

answer = float('inf')

while q:
    idx, max_num = q.popleft()

    if idx == n - 1:
        answer = min(answer, max_num)

    for i in range(1, k + 1):
        next_idx = idx + i

        if next_idx <= n - 1:
            # print(next_idx)
            # print(max_num, arr[next_idx])
            next_num = max(max_num, arr[next_idx])
            if visited[next_idx] > max_num:
                visited[next_idx] = next_num
                q.append((next_idx, next_num))

print(answer)