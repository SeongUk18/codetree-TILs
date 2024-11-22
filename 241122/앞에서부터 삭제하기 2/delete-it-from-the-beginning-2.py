import heapq

n = int(input())

num_list = list(map(int, input().split()))

max_avg = 0

for i in range(1, n - 1):
    new_num_list = num_list[i:]

    heapq.heapify(new_num_list)
    heapq.heappop(new_num_list)

    max_avg = max(max_avg, sum(new_num_list) / len(new_num_list))

print(f"{max_avg:0.2f}")