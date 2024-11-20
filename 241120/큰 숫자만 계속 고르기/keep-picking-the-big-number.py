import heapq

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

heapq.heapify(num_list)
heap = []

for n in num_list:
    # print(-n)
    heapq.heappush(heap, - n)

for _ in range(m):
    max_value = -heapq.heappop(heap)
    
    # 1 줄인 값 추가하기 - O(log N)
    heapq.heappush(heap, -(max_value - 1))


print(-heap[0])