import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []

for i in arr:
    heapq.heappush(heap, - i)
    if len(heap) == 4:
        heapq.heappop(heap)
    answer = 1

    if len(heap) == 3:
        for j in heap:
            answer *= -j
        print(answer)
    else:
        print(-1)