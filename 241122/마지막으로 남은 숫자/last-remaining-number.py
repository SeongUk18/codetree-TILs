import heapq

n = int(input())

num_list = list(map(int, input().split()))

heap = []

for i in num_list:
    heapq.heappush(heap, -i)


while len(heap) > 1:
    x = -heapq.heappop(heap)
    y = -heapq.heappop(heap)

    diff = x - y

    if diff != 0:
        heapq.heappush(heap, -diff)

if heap:
    print(-heapq.heappop(heap))
else:
    print(-1)