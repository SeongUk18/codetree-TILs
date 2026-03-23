import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []
for i in arr:
    heapq.heappush(heap,  - i)

while len(heap) > 1:
    x = heapq.heappop(heap)
    x = - x
    y = heapq.heappop(heap)
    y = - y
    num = x - y
    if num == 0:
        continue
    else:
        heapq.heappush(arr, - num)

print(- heap[0])