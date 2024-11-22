import heapq

n, m = map(int, input().split())

heap = []

for _ in range(n):
    x, y = map(int, input().split())

    heapq.heappush(heap, (abs(x) + abs(y), x, y))

for _ in range(m):
    __, cur_x, cur_y = heapq.heappop(heap)

    cur_x += 2
    cur_y += 2

    heapq.heappush(heap, (abs(cur_x) + abs(cur_y), cur_x, cur_y))

_, answer_x, answer_y = heapq.heappop(heap)

print(answer_x, answer_y)