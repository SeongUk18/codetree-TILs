import heapq

n = int(input())

heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            _, answer = heapq.heappop(heap)
            print(answer)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))