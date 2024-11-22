import heapq

n = int(input())

num_list = list(map(int, input().split()))

max_avg = 0

# 누적 합 계산
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + num_list[i]


for i in range(1, n - 1):
    new_num_list = num_list[i:]

    heapq.heapify(new_num_list)
    smallest = heapq.heappop(new_num_list)

    total_sum = prefix_sum[n] - prefix_sum[i] - smallest

    max_avg = max(max_avg, total_sum / (n - i - 1))

print(f"{max_avg:0.2f}")