import heapq

n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

pq = []

for i in range(min(n, k)):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

answer = 0
for _ in range(k):
    sum_num, i, j = heapq.heappop(pq)
    answer = sum_num

    if j + 1 < m:
        heapq.heappush(pq, (arr1[i] + arr2[j + 1], i, j + 1))

print(answer)
