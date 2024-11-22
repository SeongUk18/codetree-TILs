import heapq

n = int(input())
num_list = list(map(int, input().split()))

# 누적 합 계산
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + num_list[i]

max_avg = 0
min_heap = []
removed_set = set()

# 힙 초기화
for i in range(1, n):
    heapq.heappush(min_heap, num_list[i])

# K를 1부터 N-2까지 순회
for K in range(1, n - 1):
    # K번째 값을 제거
    removed_set.add(num_list[K - 1])

    # 유효한 최소값 찾기
    while min_heap and min_heap[0] in removed_set:  # 힙이 비어있는지 확인
        heapq.heappop(min_heap)

    if min_heap:  # 힙이 비어있지 않은 경우에만 진행
        smallest = heapq.heappop(min_heap)

        # 남아있는 합 계산
        total_sum = prefix_sum[n] - prefix_sum[K] - smallest

        # 남아있는 숫자의 평균 계산
        remaining_count = n - K - 1
        current_avg = total_sum / remaining_count

        # 최대 평균 갱신
        max_avg = max(max_avg, current_avg)

print(f"{max_avg:.2f}")
